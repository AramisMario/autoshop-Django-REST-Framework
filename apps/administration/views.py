from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import APIView
from apps.authregister.models import Mechanics, Receptionist
from apps.authregister.customPermissionClasses import AdminPermission
from apps.authregister.jwtbackend import JWTAuthentication
from apps.authregister.serializers import MechanicsSerializer, RecepcionistSerializer
import copy
import hashlib
# Create your views here.

class HireEmployee(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AdminPermission,)
    parser_classes = (FormParser,)
    render_classes = (JSONRenderer,)

    def post(self, request, format = None):
        data = request.data.copy()
        data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
        data.pop("rol")
        if request.data["rol"] == "mechanical":
            mechanic = MechanicsSerializer(data = data)
            if mechanic.is_valid():
                mechanic.save()
                return Response({"mesaje":"creado"},status = status.HTTP_201_CREATED)
        if request.data["rol"] == "receptionist":
            receptionist = RecepcionistSerializer(data = data)
            if receptionist.is_valid():
                receptionist.save()
                return Response({"mensaje":"creado"},status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
