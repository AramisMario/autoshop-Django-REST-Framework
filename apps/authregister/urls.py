from django.urls import path
from apps.authregister.views import *

urlpatterns = [
    path('signin/',SignIn.as_view()),
    path('signup/',SignIn.as_view()),
    path('testCustomer/',AuthPruebaCustomer.as_view()),
    path('testAdmin/',AuthPruebaAdmin.as_view()),
    path('testMechanic/',AuthPruebaMechanic.as_view()),
    path('testReceptionist/',AuthPruebaReceptionist.as_view()),
]
