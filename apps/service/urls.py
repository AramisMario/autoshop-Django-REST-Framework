from django.urls import path
from apps.service.views import *

urlpatterns = [
    path('registVehicle/',SaveVehicle.as_view()),
    path('listvehicles/',ShowVehicles.as_view()),
]
