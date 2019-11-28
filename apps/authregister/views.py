from django.shortcuts import render
from rest_framework.response import *
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from apps.authregister.models import *
from apps.authregister.serializers import *
import hashlib
# Create your views here.

class SaveCustomer(APIView):
    parser_classess = (FormParser,)

    def post(self,request, format=None):
        data = request.data.copy()
        data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
        Customer = CustomerSerializer(data = data)
        if Customer.is_valid():
            Customer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTT_400_BAD_REQUES)
