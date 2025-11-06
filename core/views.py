from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('nomy-options')
    return render(request, "core/home.html")

def intro(request):
    return render(request, "core/intro.html")

def options(request):
    return render(request, "core/options.html")

def about(request):
    return render(request, "core/about.html")

@login_required
def settings(request):
    return render(request, "core/settings.html")

def help(request):
    return render(request, "core/help.html")