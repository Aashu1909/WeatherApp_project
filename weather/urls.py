# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('show_temp_city', views.getWeather_city ,name='getWeatherCity'),
    path('show_temp_crd', views.getWeather_crd ,name='getWeatherCrd')
]