from django.shortcuts import render
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

        

    return render(request, 'create_appointment.html')