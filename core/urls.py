from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='nomy-home'),
    path('options/', views.options, name='nomy-options'),
    path('about/', views.about, name='nomy-about'),
    path('settings/', views.settings, name='nomy-settings'),
    path('help/', views.help, name='nomy-help'),
    path('emotionize/', include('emotionfy.urls')),
    path('dailies/', include('dailies.urls')),
    path('express/', include('express.urls')),
    path('toolkit/', include('toolkit.urls')),
]