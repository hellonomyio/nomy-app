from django.urls import path
from . import views
app_name = 'emotionfy'
urlpatterns = [
    path('', views.home, name='emotionfy-home'),
    path('emotionfy-all', views.emotionfyAll, name='emotionfy-all'),
    path('emotionfy-story/', views.emotionStory, name='emotionfy-story'),
]