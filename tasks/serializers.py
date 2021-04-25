from rest_framework import serializers

from .models import Task, TaskStatus


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['value', 'sorting']


class GoodTaskSerializer(serializers.ModelSerializer):
    fk_status = TaskStatusSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['fk_status', 'name', ]


class BadTaskSerializer(serializers.ModelSerializer):
    fsm_status = TaskStatusSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['fsm_status', 'name', ]
