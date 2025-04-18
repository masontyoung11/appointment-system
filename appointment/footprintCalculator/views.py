from django.shortcuts import render
from . import models

# Create your views here.
def carbon_quiz(request):
    if request.method == 'POST':
        energy_usage = request.POST.get('energy-usage')
        transportation = request.POST.get('personal-transport')
        public_transport = request.POST.get('public-transport-input')
        food_intake = request.POST.get('food-intake')

        # Add logic to calculate the carbon footprint based on the data
        carbon_footprint = (int(energy_usage) * 1) + (int(transportation) * 1) + (int(public_transport) * 1) + (int(food_intake) * 1)

        # Add logic to save the data to the database
        models.carbonFootprint.objects.create(
            carbon_footprint=carbon_footprint,
            # user=request.user  # Uncomment when user model is added
        )

        # Redirect to account page

    return render(request, 'carbon_footprint/carbon_footprint_quiz.html')