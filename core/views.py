from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def options(request):
    return render(request, "core/options.html")

def about(request):
    return render(request, "core/about.html")

def settings(request):
    return render(request, "core/settings.html")

def help(request):
    return render(request, "core/help.html")