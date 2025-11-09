from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from .forms import UserRegisterForm
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def create_admin(request):
    if not User.objects.filter(username="nomysarah").exists():
        User.objects.create_superuser("nomysarah", "sarah@nomy-app.com", "admin123")
        return HttpResponse("✅ Superuser created: nomysarah / admin123")
    else:
        return HttpResponse("⚠️ Superuser already exists.")
