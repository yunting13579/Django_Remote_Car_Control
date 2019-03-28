"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trips.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page,name='home'),
    path('sent_data/',sent_data,name='sent_data'),
	path('send_django/',recieve_data,name='recieve_data'),
    path('pi_car/',car_data,name='car_data'),
    path('GPS_Sheet/',GPS_Sheet,name='GPS_Sheet'),
    path('GPS_update/',GPS_Sheet_update,name='GPS_Sheet_update'),
    path('robotic_arm/',robotic_arm,name='robotic_arm'),
    path('robotic_arm_value/',robotic_arm_value,name='robotic_arm_value'),

    
]
