from django.urls import path
from apps.reception.views import *


urlpatterns = [
    path('savetbr/',SaveTaskByRef.as_view()),
    path('savet/',SaveTask.as_view()),
]
