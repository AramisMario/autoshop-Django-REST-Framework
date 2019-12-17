from django.urls import path
from apps.service.views import *

urlpatterns = [
    path('registVehicle/',SaveVehicle.as_view()),
    path('listvehicles/',ShowVehicles.as_view()),
    path('filtertasks/',RepairFilter.as_view()),
    path('filtertasksbyref/',RepairFilterByRef.as_view()),
    path('filtertaskbytag/',RepairFilterByTag.as_view()),
    path('estmoutdate/<int:id>/',EstimatedOutDate.as_view()),
    path('rstatus/<int:id>/',RepairStatus.as_view()),
    path('history/<int:id>/',ServicesHistory.as_view()),
]
