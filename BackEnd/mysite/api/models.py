# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Preference(models.Model):
    name = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=25)
    raEmail = models.CharField(max_length=25)
    rdEmail = models.CharField(max_length=25)
    RES_HALL = (
        ('Apt', 'Apartments'), ('TH','Thomas Hall'),
    ('DH', 'Davis Hall'), ('GH', 'Gilbert Hall'), ('Penn', 'Penn'),
    ('Mab', 'Mabee'), ('ELH','ELH'),('Q', 'Quads')
    )
    resHall = models.CharField(max_length = 5, choices = RES_HALL)
    floorNumber = models.CharField(max_length = 4)
    roomNumber = models.CharField(max_length = 4)

class Structure(models.Model):
    workOrderId = models.ForeignKey(Preference, on_delete=models.CASCADE)
    submissionDate = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False)

class WorkOrder(models.Model):
    Building = models.CharField(max_length = 10)
    Coordinates = models.CharField(max_length = 10)
    Description = models.TextField(max_length=45)
    preferencesID = models.ForeignKey(Preference, on_delete=models.CASCADE)

    class Meta:
        model = Preference
        fields = ['name','raEmail','rdEmail']





