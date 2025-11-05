from django.shortcuts import render, redirect

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

def settings(request):
    return render(request, "core/settings.html")

def help(request):
    return render(request, "core/help.html")