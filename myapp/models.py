from django.db import models
# Create your models here.
#create patient model with attribute name,age,address,phone_number
class Patient(models.Model):
    name = models.CharField(max_length=20)
    age= models.IntegerField()
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)
# create Doctor model with choices and attributes
class Doctor(models.Model):
    # Choices give options in dropdown
    # Model have attributes in foam of choices,doc_type and name
    DOC_CHOICES = [
        ('Children', 'child'),
        ('Dermatologist', 'dmt'),
        ('Doctor of Medicine', 'md'),
        ('Osteopathic Medicine', 'do'),
    ]    
    doc_type = models.CharField(choices=DOC_CHOICES , max_length=50)
    name = models.CharField(max_length=20)

    # String Representation
    def __str__(self) -> str:
        return self.name    
# Forign relationship (one to many)
class DoctorPatient(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    
# Model with many to many realtionship
class Medician(models.Model):
    assigned = models.ManyToManyField(DoctorPatient, related_name="doctorpatient")


class tables(models.Model):
    which_doc = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    which_pat = models.ForeignKey(Patient,on_delete=models.CASCADE)
    which_med = models.ForeignKey(Medician,on_delete=models.CASCADE)