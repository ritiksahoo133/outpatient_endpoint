from django.contrib import admin
from appointment.models import Doctor, Appointment

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "max_patient"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "doctor", "date", "time", "patient_name"]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
