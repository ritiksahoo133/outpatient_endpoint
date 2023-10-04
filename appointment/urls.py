from django.urls import path
from .views import CreateDoctor, DoctorList, BookAppointment

urlpatterns = [
    path("create-doctor", CreateDoctor.as_view(), name="create-doctor"),
    path("doctors", DoctorList.as_view(), name="doctors"),
    path("book-appointment", BookAppointment.as_view(), name="book-appointment"),
]
