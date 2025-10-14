from django.urls import path
from .views import home, dismiss_signup_prompt

urlpatterns = [
    path('emotionfy/', home, name='home'),
    path('api/prompt/dismiss/', dismiss_signup_prompt, name='dismiss_signup_prompt'),
]
