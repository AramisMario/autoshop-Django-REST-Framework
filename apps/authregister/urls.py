from django.urls import path
from apps.authregister.views import *

urlpatterns = [
    path('register/',SaveCustomer.as_view()),
    path('login/',Login.as_view()),
    path('test/',AuthPrueba.as_view()),
]
