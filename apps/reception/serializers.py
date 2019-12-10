from rest_framework import serializers
from apps.service.models import Tasksbyref, Tasks, Details, Services


class TasksbyrefSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(queryset = Tasks.objects.all())
    class Meta:
        model = Tasksbyref
        fields = ('price','tdescription','tasks','estimatedtime','refsallowed')

    def create(self, validated_data):
        tasksbyref = Tasksbyref.objects.create(price = validated_data["price"],
        tdescription = validated_data["tdescription"],
        tasks = validated_data["tasks"],
        estimatedtime = validated_data["estimatedtime"],refsallowed = validated_data["refsallowed"])
        return tasksbyref

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('task','tag')

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('description','tasks','services','mechanics')

    def create(self,validated_data):
        details = Details.objects.create(description = validated_data["description"],
        tasks = validated_data["tasks"], services = validated_data["services"],
        mechanics = validated_data["mechanics"])
        return details

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id','indate','outdate','vehicles','receptionist')

    def create(self, validated_data):
        service = Services.objects.create(indate = validated_data["indate"],
        outdate = validated_data["outdate"], vehicles = validated_data["vehicles"],
        receptionist = validated_data["receptionist"])
        return service
