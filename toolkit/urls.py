from django.urls import path
from . import views
app_name = 'toolkit'
urlpatterns = [
    path('', views.home, name='toolkit-home'),
    path('options/', views.options, name='toolkit-options'),
    path('breathing/', views.breathing, name='toolkit-breathing'),
    path('breathing/box', views.boxBreathing, name='toolkit-box-breathing'),
    path('breathing/triangle', views.triangleBreathing, name='toolkit-triangle-breathing'),
    path('breathing/extended-exhale', views.extendedExhale, name='toolkit-extended-exhale'),
    path('puzzles/', views.puzzles, name='toolkit-puzzles'),
    path('puzzles/memory-pairing', views.memoryPairing, name='toolkit-memory-pairing'),

]