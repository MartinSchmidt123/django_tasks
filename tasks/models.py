from django.db import models
from django_fsm import FSMKeyField


class TaskStatus(models.Model):
    value = models.CharField(max_length=50, primary_key=True)
    sorting = models.IntegerField()


class Task(models.Model):
    name = models.CharField(max_length=50)
    fk_status = models.ForeignKey(TaskStatus, default='draft', on_delete=models.CASCADE,related_name='+')
    fsm_status = FSMKeyField(TaskStatus, default='draft', on_delete=models.CASCADE,related_name='+')
