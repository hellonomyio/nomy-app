from django.urls import path
from . import views
app_name = 'dailies'
urlpatterns = [
    path('', views.home, name='dailies-home'),
    path('morning-affirmation/', views.dailiesMorningAffirmation, name='morningAffirmation'),
    path('morning-goal/', views.dailiesMorningGoal, name='morningGoal'),
    path('evening/', views.dailiesEvening, name='evening'),
    path('dailies-story/', views.dailiesStory, name='dailies-story'),
]