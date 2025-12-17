from django.urls import path
from . import views
app_name = 'express'
urlpatterns = [
    path('', views.home, name='express-home'),
    path('create/', views.createScenarioPage, name='create-scenario'),
    path('custom/', views.expressCustom, name='express-custom'),
    path('speak/', views.expressSpeak, name='express-speak'),
    path('text/', views.expressText, name='express-text'),
    path('scenario/', views.expressScenario, name='express-scenario'),
    path('response/', views.expressResponse, name="express-response"),
]