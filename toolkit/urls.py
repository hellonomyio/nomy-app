from django.urls import path
from . import views
app_name = 'toolkit'
urlpatterns = [
    path('', views.home, name='toolkit-home'),
    path('options/', views.options, name='toolkit-options'),
    path('breathing/', views.breathing, name='toolkit-breathing'),
    path('box/breathing/', views.boxBreathing, name='toolkit-box-breathing'),
    path('puzzles/', views.puzzles, name='toolkit-puzzles'),
]