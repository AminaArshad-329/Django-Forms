from django import forms
from .models import *
from django.shortcuts import render , redirect

# Creating form
class DoctorRegistraion(forms.ModelForm):
    #takinfg doc_id from doctor model
    doc_id = forms.ModelChoiceField(queryset=Doctor.objects.all())
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientRegistraion(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorPatientRegistraion(forms.ModelForm):
    class Meta:
        model = DoctorPatient
        fields =  '__all__'

class MedicianRegistraion(forms.ModelForm):
    # med_id = forms.ModelChoiceField(queryset=Medician.objects.all())
    class Meta:
        model = Medician
        fields =  '__all__'

class TableRegistraion(forms.ModelForm):
    class Meta:
        model = tables
        fields =  '__all__'