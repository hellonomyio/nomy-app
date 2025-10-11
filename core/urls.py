from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='nomy-home'),
    path('options/', views.options, name='nomy-options'),
    path('emotionfy/', include('emotionfy.urls')),
    path('dailies/', include('dailies.urls')),
]