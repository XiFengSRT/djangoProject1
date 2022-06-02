from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=64,primary_key=True)
    password = models.CharField(max_length=64)
    showName = models.CharField(max_length=64)
    wallet = models.IntegerField()

#
# class rechargeRequest(models.Model):
#     userName = models.CharField(max_length=64)
#     date = models.DateTimeField()
#     recharge = models.IntegerField()
#     accpet = models.BooleanField()
