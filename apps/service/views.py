from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.authregister.jwtbackend import JWTAuthentication
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from apps.service.models import *
from apps.service.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser
from rest_framework import status
# Create your views here.

class SaveVehicle(APIView):

    authentication_classes = ()
    permission_classes = ()
    parser_classes = (FormParser,)
    #authentication_classes = (JWTAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def post(self, request, format = None):
        vehicle = VehicleSerializer(data = request.data)
        if vehicle.is_valid():
            vehicle.save()
            return Response({"mensaje":"creado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"bad request"},status = status.HTTP_400_BAD_REQUEST)


class ShowVehicles(APIView):

    authentication_classes = ()
    permission_classes = ()
    render_classes = (JSONRenderer,)
    def get(self, request, format = None):
        vehicles = Vehicles.objects.all()
        vehiclesSerialized = VehicleSerializer(vehicles, many = True)
        context = {"vehicles":vehiclesSerialized.data}
        return Response(context, status.HTTP_200_OK)
