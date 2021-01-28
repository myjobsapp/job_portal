from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ch = (('Service Based','Service Based'),
      ('Product Based','Product Based'),
      ('Startup','Startup'))

class CompanyModel(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    loc = models.CharField(max_length=40)
    type = models.CharField(max_length=30,choices=ch)
    domain = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class JobModel(models.Model):
    company = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)
    desg= models.CharField(max_length=40)
    ctc = models.FloatField()
    exp = models.FloatField()
    loc = models.CharField(max_length=30)
    skills = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.desg}'




