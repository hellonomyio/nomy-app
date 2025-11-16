from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def debug_email(request):
    return JsonResponse({
        "EMAIL_HOST": settings.EMAIL_HOST,
        "EMAIL_PORT": settings.EMAIL_PORT,
        "EMAIL_USE_TLS": settings.EMAIL_USE_TLS,
        "EMAIL_HOST_USER": settings.EMAIL_HOST_USER,
        "EMAIL_HOST_PASSWORD_SET": bool(settings.EMAIL_HOST_PASSWORD),
        "DEFAULT_FROM_EMAIL": settings.DEFAULT_FROM_EMAIL,
    })

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = "Welcome to NOMY"
            message = (
                f"Hi {user.username},\n\n"
                "Thank you for creating an account with NOMY.\n"
                "We're excited to have you here.\n\n"
                "You can now log in anytime.\n\n"
                "The NOMY Team"
            )
            recipient = user.email

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                fail_silently=False,
            )

            messages.success(request, "Your account has been created! Please check your email 💌")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
