from django.shortcuts import render, redirect
from .models import Appointments

# Create your views here.
def create_appointment(request):
    if request.method == "POST":
        bedroom_to_energy_map = {
            "low-bedrooms": 7500,
            "medium-bedrooms": 11500,
            "high-bedrooms": 17000,
        }

        appointment_type = request.POST.get('installation-type')
        energy_usage = request.POST.get('bedroom-amm')
        time_choice = request.POST.get('time-choice')
        date = request.POST.get('date')

        if energy_usage == "custom-bedrooms-input":
            energy_usage = request.POST.get('custom-bedrooms-input')
        else:
            energy_usage = bedroom_to_energy_map.get(energy_usage, 1)


        Appointments.objects.create(type=appointment_type, energy_usage=energy_usage, time_choice=time_choice, date=date)
        return redirect('view_appointments')  # Redirect to a view that lists all appointments
        

    return render(request, 'create_appointment.html')


def view_appointments(request):
    appointments = Appointments.objects.all()

    return render(request, 'view_appointments.html', {'appointments': appointments})


def complete_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointments.objects.get(id=appointment_id)

        appointment.delete()  # Delete the appointment
        return redirect('view_appointments')  # Redirect to a view that lists all appointments

    return render(request, 'view_appointments.html')