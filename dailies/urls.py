from django.urls import path
from . import views
app_name = 'dailies'
urlpatterns = [
    path('', views.home, name='dailies-home'),
]