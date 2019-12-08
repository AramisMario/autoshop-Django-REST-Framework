from django.urls import path
from apps.administration.views import *

urlpatterns = [

    path('saveEmployee/',HireEmployee.as_view()),

]
