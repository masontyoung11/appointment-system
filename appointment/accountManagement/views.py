from django.shortcuts import render
from appointment_management.models import Appointments

# Create your views here.
def settings(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'account_modification':
            first_name = request.POST.get('first_name')

            # Retrieve the rest of the user's information from the form.
            # Update the user's information in the database.
            # For example:
            # user = request.user
            # user.first_name = first_name
            # user.save()
            
        elif form_type == 'appointment_modification':
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointments.objects.get(id=appointment_id)

            # Retrieve the rest of the appointment's information from the form.
            # Update the appointment's information in the database.
            # For example:
            # appointment.date = request.POST.get('date')
            # appointment.save()



    appointments = Appointments.objects.all()

    return render(request, 'accountManagement/settings.html', {'appointments': appointments})