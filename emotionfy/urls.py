from django.urls import path
from . import views
app_name = 'emotionfy'
urlpatterns = [
    path('', views.home, name='emotionize-home'),
    path('emotionize-all', views.emotionizeAll, name='emotionize-all'),
    path('emotionize-story/', views.emotionizeStory, name='emotionize-story'),
]