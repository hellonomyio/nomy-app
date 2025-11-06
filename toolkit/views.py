from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'toolkit/home.html')

def breathing(request):
    return render(request, 'toolkit/breathing.html')

def boxBreathing(request):
    return render(request, 'toolkit/box-breathing.html')

def puzzles(request):
    return render(request, 'toolkit/puzzles.html')

def options(request):
    return render(request, 'toolkit/options.html')