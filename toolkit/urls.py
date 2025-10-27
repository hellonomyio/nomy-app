from django.urls import path
from . import views
app_name = 'toolkit'
urlpatterns = [
    path('', views.home, name='toolkit-home'),
    path('options/', views.options, name='toolkit-options'),
]