from django.shortcuts import render

# Create your views here.
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

def options(request):
    return render(request, 'toolkit/options.html')