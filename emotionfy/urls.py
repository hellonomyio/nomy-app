from django.urls import path
from . import views
app_name = 'emotionfy'
urlpatterns = [
    path('', views.home, name='emotionize-home'),
    path('all', views.emotionizeAll, name='all'),
    path('story/', views.emotionizeStory, name='story'),
    path('intro/', views.emotionizeIntro, name='intro'),
    path('energised/', views.emotionizeEnergised, name='energised'),
    path('pleasant/', views.emotionizePleasant, name='pleasant'),
    path('low-energy/', views.emotionizeLowEnergy, name='low-energy'),
    path('vulnerable/', views.emotionizeVulnerable, name='vulnerable'),
]