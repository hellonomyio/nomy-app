from django.urls import path
from . import views
app_name = 'express'
urlpatterns = [
    path('', views.home, name='express-home'),
    path('express-intro/', views.expressIntro, name='express-intro'),
]