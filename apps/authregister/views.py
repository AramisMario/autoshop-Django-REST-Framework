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
from rest_framework.authentication import get_authorization_header
from apps.authregister.custompermissionclasses import *
import os
import jwt, json
# Create your views here.

class SignUp(APIView):
    parser_classess = (MultiPartParser,)
    authentication_classes = ()
    def post(self,request, format=None):
        data = request.data.copy()
        data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
        customer = CustomerSerializer(data = data)
        if customer.is_valid():
            customer.save()
            return Response({"mensaje":"guardado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"},status = status.HTTP_400_BAD_REQUEST)

class SignIn(APIView):
    parser_classes = (FormParser,)
    authentication_classes = ()
    def post(self,request,format = None):
        data = request.data.copy()
        data['password'] = hashlib.sha256(request.data['password'].encode()).hexdigest()
        if data['rol'] == "customer":
            try:
                customer = Customers.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el customer"})
            else:
                return Response({'token':customer.token})

        elif data['rol'] == "mechanical":
            try:
                mechanic = Mechanics.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el mechanic"})
            else:
                return Response({'token':mechanic.token})

        elif data['rol'] == "receptionist":
            try:
                receptionist = Receptionist.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el receptionist"})
            else:
                return Response({'token':receptionist.token})

        elif data['rol'] == "admin":
            try:
                admin = Admins.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el admin"})
            else:
                return Response({'token':admin.token})
        return Response({'mensaje':'algo fue mal'})

class AuthPruebaReceptionist(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (ReceptionistPermission,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste receptionist"})

class AuthPruebaMechanic(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (MechanicsPermission,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste mechanic"})

class AuthPruebaCustomer(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (CustomersPermission,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste customer"})

class AuthPruebaAdmin(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (AdminPermission,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste admin"})
