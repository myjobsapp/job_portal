from django.db import models
from django.db.models import F

# Create your models here.

class EmployeeModel(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    eaddr = models.CharField(max_length=40)
    esalary = models.FloatField()

    def __str__(self):
        return self.ename
