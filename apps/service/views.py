from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.authregister.jwtbackend import JWTAuthentication
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from apps.service.models import *
from apps.service.serializers import *
from apps.reception.serializers import TaskSerializer, TaskbyrefSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser, JSONParser
from rest_framework import status
# Create your views here.

class SaveVehicle(APIView):

    parser_classes = (FormParser,)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

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

class RepairFilter(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def post(self, request, format = None):
        repairs = Tasksbyref.objects.all()
        repairsSerialized = TaskbyrefSerializer(repairs,many = True)
        context = {"repairs":repairsSerialized.data}
        return Response(context,status = status.HTTP_200_OK)

class RepairFilterByRef(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def post(self, request, format = None):
        tasks = Task.customManager.tasksbyref(request.data["ref"])
        return Response(tasks,status = status.HTTP_200_OK)

class  RepairFilterByTag(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def post(self, request, format = None):
        repairs = Task.objects.filter(tag__contains = request.data["tag"])
        repairsSerialized = TaskSerializer(repairs,many = True)
        context = {"repairs":repairsSerialized.data}
        return Response(context,status = status.HTTP_200_OK)
