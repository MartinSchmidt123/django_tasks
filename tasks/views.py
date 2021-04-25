from rest_framework import viewsets

from .models import Task
from .serializers import BadTaskSerializer, GoodTaskSerializer


class GoodTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = GoodTaskSerializer


class BadTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = BadTaskSerializer
