from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from rest_framework import status

# Create your views here.


class CreateDoctor(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def create(self, request, *args, **kwargs):
        doctor_name = request.data.get("name", None)
        if doctor_name and Doctor.objects.filter(name=doctor_name).exists():
            return Response(
                {"error": "Doctor with this name already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request)


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class BookAppointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        doctor = serializer.validated_data["doctor"]
        print(type(doctor.max_patient))
        date = serializer.validated_data["date"]

        appointment_count = Appointment.objects.filter(doctor=doctor, date=date).count()
        if appointment_count >= doctor.max_patient:
            raise serializers.ValidationError(
                "Doctor has reached the maximum appointments"
            )
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
