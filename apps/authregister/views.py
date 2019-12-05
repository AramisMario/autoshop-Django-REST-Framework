from django.shortcuts import render
from rest_framework.response import *
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import JSONParser
from apps.authregister.models import *
from apps.authregister.serializers import *
from rest_framework.permissions import IsAuthenticated
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from apps.authregister.jwtbackend import JWTAuthentication
# Create your views here.

class SaveCustomer(APIView):
    parser_classess = (MultiPartParser,)
    authentication_classes = ()
    def post(self,request, format=None):
        data = request.data.copy()
        data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
        mecanico = MechanicsSerializer(data = data)
        if mecanico.is_valid():
            mecanico.save()
            return Response({"mensaje":"guardado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"},status = status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    parser_classess = (FormParser,)
    authentication_classes = ()
    def post(self,request,format = None):
        # data = request.data.copy()
        request.data['password'] = hashlib.sha256(request.data['password'].encode()).hexdigest()
        try:
            customer = Customers.objects.get(email = request.data['email'], password = request.data['password'])
        except ObjectDoesNotExist:
            return Response({"mensaje":"No exite el usuario"})
        return Response({'token':customer.token})

class AuthPrueba(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste"})
