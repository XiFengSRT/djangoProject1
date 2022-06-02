from django.db import models
from django.db.models.signals import post_save
from User.models import User


# Create your models here.
class rechargeRequest(models.Model):
    userName = models.CharField(max_length=64)
    date = models.DateTimeField()
    recharge = models.IntegerField()
    accpet = models.BooleanField()
    finish = models.BooleanField(default=False)

    def accpet_recharge(self):
        print(self.accpet)
        if self.accpet == True and self.finish == False:
            self.finish = True
            self.save()
            _t = User.objects.filter(userName=self.userName).first()
            _t.wallet = _t.wallet + self.recharge
            _t.save()
        if self.finish:
            return "已经完成充值"
        else:
            return "未完成充值"
