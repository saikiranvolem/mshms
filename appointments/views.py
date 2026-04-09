from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment

# Create your views here.
@login_required
def appointment_list(request):
    appoinments = Appointment.objects.all()
    return render(request, 'app_list.html', {'appointments': appoinments})

@login_required
def appointment_create(request):
    if request.method == "POST":
        # Getting data from the form (matching the 'name' attributes in the HTML)
        doctor = request.POST.get('doctor')
        patient = request.POST.get('patient')
        time = request.POST.get('time')
        
        Appointment.objects.create(
            doctor_name=doctor, 
            patient_name=patient, 
            time=time
        )
        return redirect('appointment_list')
    return render(request, 'app_create.html')

@login_required
def appointment_edit(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    
    if request.method == "POST":
        appointment.doctor_name = request.POST.get('doctor')
        appointment.patient_name = request.POST.get('patient')
        appointment.time = request.POST.get('time')
        appointment.save()
        return redirect('appointment_list')
        
    return render(request, 'app_edit.html', {'appointment': appointment})

@login_required
def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('appointment_list')