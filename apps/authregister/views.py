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

class SaveSomeRol(APIView):
    parser_classes = (FormParser,)
    authentication_classes = ()
    def post(self,request, format=None):
        data = request.data.copy()
        data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
        admin = AdminsSerializer(data = data)
        if admin.is_valid():
            admin.save()
            return Response({"mensaje":"guardado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"},status = status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    parser_classes = (FormParser,)
    authentication_classes = ()
    def post(self,request,format = None):
        data = request.data.copy()
        data['password'] = hashlib.sha256(request.data['password'].encode()).hexdigest()
        if data['rol'] == "customer":
            try:
                customer = Customers.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el usuario"})
            else:
                return Response({'token':customer.token})

        elif data['rol'] == "mechanical":
            try:
                mechanic = Mechanics.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el usuario"})
            else:
                return Response({'token':mechanic.token})

        elif data['rol'] == "receptionist":
            try:
                receptionist = Receptionist.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el usuario"})
            else:
                return Response({'token':receptionist.token})

        elif data['rol'] == "admin":
            try:
                admin = Admins.objects.get(email = data['email'], password = data['password'])
            except ObjectDoesNotExist:
                return Response({"mensaje":"No exite el usuario"})
            else:
                return Response({'token':admins.token})
        return Response({'mensaje':'algo fue mal'})

class AuthPrueba(APIView):
    autentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request, format = None):
        return Response({"mensaje":"te autenticaste"})
