from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'express/home.html')

def expressIntro(request):
    return render(request, "express/express-intro.html")