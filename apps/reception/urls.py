from django.urls import path
from apps.reception.views import *


urlpatterns = [
    path('savetbr/',SaveTasksByRef.as_view()),
    path('savet/',SaveTasks.as_view()),
    path('savedtl/',SaveDetails.as_view()),
    path('services/',ServicesView.as_view()),
]
