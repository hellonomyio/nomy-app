from django.urls import path
from . import views

urlpatterns = [
    path("save/express/", views.save_express, name="save_express"),
    path("save/emotion/", views.save_emotion, name="save_emotion"),
    path("get/emotion/", views.get_emotion_reflections, name="get_emotion"),
]
