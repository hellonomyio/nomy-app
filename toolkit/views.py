from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'toolkit/home.html')

def options(request):
    return render(request, 'toolkit/options.html')