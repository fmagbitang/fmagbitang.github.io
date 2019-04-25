from django.db import models
from math import *

class Triangle(models.Model):
    length1 = models.CharField(max_length=100, null=True)
    length2 = models.CharField(max_length=100, null=True)
    length3 = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    perimeter = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE,  null=True)

    class Meta:
        ordering = ('created_at',)
