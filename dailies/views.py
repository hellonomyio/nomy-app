from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dailies/home.html')

def dailiesMorning(request):
    return render(request, 'dailies/dailies-morning.html')

def dailiesEvening(request):
    return render(request, 'dailies/dailies-evening.html')