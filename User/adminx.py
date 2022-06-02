from django.contrib import admin

# Register your models here.
import xadmin
from User.models import User


class UserAdmin(object):
    list_display = (
        'showName',
        'userName',
        'wallet'
    )




xadmin.site.register(User, UserAdmin)

