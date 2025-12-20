from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "core/home.html")

@login_required
def intro(request):
    return render(request, "core/intro.html")

@login_required
def options(request):
    return render(request, "core/options.html")

@login_required
def about(request):
    return render(request, "core/about.html")

@login_required
def settings(request):
    return render(request, "core/settings.html")

@login_required
def help(request):
    return render(request, "core/help.html")