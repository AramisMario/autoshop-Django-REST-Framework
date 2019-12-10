from rest_framework import serializers
from apps.service.models import Tasksbyref
from apps.service.models import Tasks

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
