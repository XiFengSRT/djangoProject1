from django.contrib import admin
import xadmin
# Register your models here.
from recharge.models import rechargeRequest


class rechargeRequestAdmin(object):
    list_display = (
        'userName',
        'date',
        'recharge',
        'accpet',
        'accpet_recharge',
    )
    list_editable = ["accpet"]


xadmin.site.register(rechargeRequest, rechargeRequestAdmin)
class pro(object):
    list_display = (
        'userName',
        'date',
        'recharge',
        'accpet',
        'accpet_recharge',
    )
    list_editable = ["accpet"]