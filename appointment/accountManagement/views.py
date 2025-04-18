from django.shortcuts import render
from appointment_management.models import Appointments

# Create your views here.
def settings(request):
    appointments = Appointments.objects.all()

    return render(request, 'accountManagement/settings.html', {'appointments': appointments})