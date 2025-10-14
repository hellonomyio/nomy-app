from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "core/home.html")

def options(request):
    return render(request, "core/options.html")

