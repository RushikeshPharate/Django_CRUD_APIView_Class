from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Student(models.Model):
    name = CharField(max_length=50)
    roll = IntegerField()
    city = CharField(max_length=20)

    


