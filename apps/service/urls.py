from django.urls import path
from apps.service.views import *

urlpatterns = [
    path('registVehicle/',SaveVehicle.as_view()),
    path('listvehicles/',ShowVehicles.as_view()),
    path('filtertasks/',RepairFilter.as_view()),
    path('filtertasksbyref/',RepairFilterByRef.as_view()),
    path('filtertaskbytag/',RepairFilterByTag.as_view()),
]
