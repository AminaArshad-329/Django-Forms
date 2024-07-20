from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DoctorPatient)
# admin.site.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display: ('id','name','email','age','address','phone_number')
