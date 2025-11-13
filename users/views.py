from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )

            messages.success(request, "Your account has been created! Please check your email 💌")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def reset_admin_password(request):
    try:
        user = User.objects.get(username="admin")
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            username="nomyadmin",
            email="hello@nomy-app.com",
            password="Saadia11"
        )

    user.set_password("Saadia11")
    user.save()

    return HttpResponse("Admin password reset. DELETE THIS VIEW NOW.")