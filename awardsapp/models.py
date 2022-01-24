from django.db import models

# Create your models here.


class Person(models.Model):
    personFirstName = models.CharField(max_length=64)
    personSurName = models.CharField(max_length=64, null=True)
    personEmail = models.CharField(max_length=64, null=True )
    personPhone = models.IntegerField()
    personGender = models.CharField(max_length=12)
    personCounter = models.IntegerField()	
    personDoesHeKnow = models.CharField(max_length=12)
    personFineorNot = models.CharField(max_length=12)
    personAgeGroup = models.CharField(max_length=12)

class Ips(models.Model):
    theIp = models.CharField(max_length=70)
    
