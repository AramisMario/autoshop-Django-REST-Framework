from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.authregister.jwtbackend import JWTAuthentication
from rest_framework.authentication import get_authorization_header
from apps.authregister.custompermissionclasses import *
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from apps.service.models import *
from apps.service.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser, JSONParser
from rest_framework import status
from rest_condition import Or
import jwt, os

# Create your views here.

class SaveVehicle(APIView):

    parser_classes = (FormParser,)
    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]

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
    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def get(self, request, format = None):
        repairs = Tasksbyref.objects.all()
        repairsSerialized = TasksbyrefSerializer(repairs,many = True)
        context = {"repairs":repairsSerialized.data}
        return Response(context,status = status.HTTP_200_OK)

class RepairFilterByRef(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def get(self, request, ref, format = None):
        tasks = Tasks.customManager.tasksbyref(ref)
        return Response(tasks,status = status.HTTP_200_OK)

class  RepairFilterByTag(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    parser_classes = (JSONParser,)
    render_classes = (JSONRenderer,)

    def get(self, request, format = None):
        repairs = Tasks.objects.filter(tag__contains = request.data["tag"])
        repairsSerialized = TasksSerializer(repairs,many = True)
        context = {"repairs":repairsSerialized.data}
        return Response(context,status = status.HTTP_200_OK)

class EstimatedOutDate(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (CustomersPermission,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, id, format = None):
        service = Services.objects.get(pk = id)
        eOutTime = service.estimatedOutDate()
        return Response({"eOutTime":eOutTime},status = status.HTTP_200_OK)

class RepairStatus(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    render_classes = (JSONRenderer,)

    def get(self, request, id, format = None):
        vehicle = Vehicles.objects.get(pk = id)
        repstatus = vehicle.status()
        return Response(repstatus,status = status.HTTP_200_OK)

class ServicesHistory(APIView):

    authentication_classes = (JWTAuthentication,)
    # permission_classes = (Or(CustomersPermission, ReceptionistPermission),)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    render_classes = (JSONRenderer,)

    def get(self, request, format = None):
        token = get_authorization_header(request).split()[1]
        payload = jwt.decode(token, os.environ["SECRETKEY"])
        history = Services.customManager.historyByCustomer(payload["id"])
        return Response(history, status = status.HTTP_200_OK)

class generateInvoice(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = [CustomersPermission | ReceptionistPermission]
    renderer_classes = (JSONRenderer,)
    def get(self, request, id, format = None):
        invoice = Services.customManager.invoiceByService(id)
        return Response(invoice,status = status.HTTP_200_OK)
