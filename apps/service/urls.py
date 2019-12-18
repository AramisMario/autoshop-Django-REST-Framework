from django.urls import path
from apps.service.views import *

urlpatterns = [
    path('registVehicle/',SaveVehicle.as_view()),
    path('listvehicles/',ShowVehicles.as_view()),
    path('filtertasks/',RepairFilter.as_view()),
    path('filtertasksbyref/<int:ref>/',RepairFilterByRef.as_view()),
    path('filtertaskbytag/',RepairFilterByTag.as_view()),
    path('estmoutdate/<int:id>/',EstimatedOutDate.as_view()),
    path('rstatus/<int:id>/',RepairStatus.as_view()),
    path('history/',ServicesHistory.as_view()),
    path('invoice/<int:id>/',generateInvoice.as_view()),
]
