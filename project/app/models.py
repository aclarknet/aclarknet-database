from django.db import models
from .utils import class_name_pk

# Create your models here.


class Client(models.Model):
    """
    """

    name = models.CharField(max_length=300)
    address = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Invoice(models.Model):
    """
    """

    client = models.ForeignKey(Client, blank=True, null=True)
    project = models.ForeignKey('Project', blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Task(models.Model):
    """
    """
    entry = models.DurationField(default='1:00')
    project = models.ForeignKey('Project', blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Project(models.Model):
    """
    """

    name = models.CharField(max_length=300, blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    client = models.ForeignKey(Client)

    def __unicode__(self):
        return class_name_pk(self)
