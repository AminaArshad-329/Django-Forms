# from django.shortcuts import render
# from .forms import *
# from django.views.generic.list import ListView
# from django.urls import reverse
# from multi_form_view import MultiModelFormView

from django.shortcuts import render , redirect
from .forms import *
from .models import *
# Create your views here.
def docdata(request):
    sf = PatientRegistraion()
    df = DoctorPatientRegistraion()
    mf = MedicianRegistraion()
    return render(request,'myapp/hospital.html',{'form':sf, "dform":df,"mform":mf})
    

def docpostdata(request):
    #Post method(adding data to db)
    if request.method == 'POST':
        print(request.POST)
        #get name,age,address,phone_number from request.POST DICT
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        #create Patient recored
        sf = Patient.objects.create(
            name=name,
            age=age,
            address=address,
            phone_number=phone_number,)
        #Save data
        sf.save()
        doc = Doctor.objects.get(id=1)
        #Create DoctorPatient record
        # doctor = request.POST.get('doctor')
        # patient = request.POST.get('id')
        df = DoctorPatient.objects.create(
            doctor=doctor,
            patient=sf,)
        df.save()
        #Check validation
        # if df.is_valid():
        #     df.save()
            #Create MedicianRegistraion record
            # mf = MedicianRegistraion(request.POST)
            # if mf.is_valid():
            #     mf.save()
    return redirect('/register/')