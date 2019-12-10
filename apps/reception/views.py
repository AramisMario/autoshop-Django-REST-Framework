from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from apps.reception.serializers import TasksbyrefSerializer, TasksSerializer, DetailsSerializer, ServicesSerializer
from apps.service.models import Services
import json
# Create your views here.


class SaveTasksByRef(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
    def post(self, request, format = None):
        request.data["refsallowed"] = json.dumps(request.data["refsallowed"])
        taskbyref = TasksbyrefSerializer(data = request.data)
        if taskbyref.is_valid():
            taskbyref.save()
            return Response({"mensaje":"creado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"},status = status.HTTP_400_BAD_REQUEST)

class SaveTasks(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
    def post(self, request, format = None):
        task = TasksSerializer(data = request.data)
        if task.is_valid():
            task.save()
            return Response({"mensaje":"creado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"},status = status.HTTP_400_BAD_REQUEST)


class SaveDetails(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
    def post(self, request, format = None):
        detail = DetailsSerializer(data = request.data)
        if detail.is_valid():
            detail.save()
            return Response({"mensaje":"creado"},status = status.HTTP_201_CREATED)
        return Response({"mensaje":"algo fue mal"}, status = status.HTTP_400_BAD_REQUEST)


class ServicesView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
    def post(self, request, format = None):
        service = ServicesSerializer(data = request.data)
        if service.is_valid():
            service.save()
            return Response({"mensaje":"creado"}, status = status.HTTP_201_CREATED)
        return Response({"mensaje":"creado"}, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        services = Services.objects.all()
        servicesSerialized = ServicesSerializer(services, many = True)
        context = {"services":servicesSerialized.data}
        return Response(context, status = status.HTTP_200_OK)
