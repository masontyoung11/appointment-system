from django.shortcuts import render

# Create your views here.
def carbon_quiz(request):
    return render(request, 'carbon_footprint_quiz.html')