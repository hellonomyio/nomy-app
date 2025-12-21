from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'toolkit/home.html')

def breathing(request):
    return render(request, 'toolkit/breathing.html')

def boxBreathing(request):
    return render(request, 'toolkit/box-breathing.html')

def triangleBreathing(request):
    return render(request, 'toolkit/triangle-breathing.html')

def extendedExhale(request):
    return render(request, 'toolkit/extended-exhale.html')

def puzzles(request):
    return render(request, 'toolkit/puzzles.html')

def memoryPairing(request):
    return render(request, 'toolkit/memory-pairing.html')

def matchObject(request):
    return render(request, 'toolkit/match-object.html')

def options(request):
    return render(request, 'toolkit/options.html')