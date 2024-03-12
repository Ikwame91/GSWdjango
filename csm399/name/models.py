from django.db import models

# Create your models here.
class Memeber(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, )
    joined_date = models.DateField( null=True, )