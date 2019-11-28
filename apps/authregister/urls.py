from django.urls import path
from apps.authregister.views import *

urlpatterns = [
    path('register/',SaveCustomer.as_view()),
]
