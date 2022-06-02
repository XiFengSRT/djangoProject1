import xadmin
from django.contrib import admin
from .models import *


# Register your models here.
class productAdmin(object):
    list_display = (
        'price',
        'showName',
        'description',
        'html_address',
        'css_address',
        'js_address'
    )


xadmin.site.register(product, productAdmin)


class propertyAdmin(object):
    list_display = (
        'userName',
        'productName'
    )


xadmin.site.register(property, propertyAdmin)
