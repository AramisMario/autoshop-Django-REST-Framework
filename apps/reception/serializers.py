from rest_framework import serializers
from apps.service.models import Tasksbyref
from apps.service.models import Task

class TaskbyrefSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(queryset = Task.objects.all())
    class Meta:
        model = Tasksbyref
        fields = ('price','tdescription','task','estimatedtime','refsallowed')

    def create(self, validated_data):
        tasksbyref = Tasksbyref.objects.create(price = validated_data["price"],
        tdescription = validated_data["tdescription"],
        task = validated_data["task"],
        estimatedtime = validated_data["estimatedtime"],refsallowed = validated_data["refsallowed"])
        return tasksbyref

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task','tag')
