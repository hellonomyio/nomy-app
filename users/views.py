from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings

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
