from django.urls import path
from . import views
app_name = 'dailies'
urlpatterns = [
    path('', views.home, name='dailies-home'),
    path('morning/', views.dailiesMorning, name='morning'),
    path('evening/', views.dailiesEvening, name='evening'),
]