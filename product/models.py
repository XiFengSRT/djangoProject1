from django.db import models


# Create your models here.
class product(models.Model):
    showName = models.CharField(max_length=64, primary_key=True)
    price = models.IntegerField()
    description = models.TextField()
    html_address = models.FileField(upload_to='FileRestore/templates', default='none')
    css_address = models.FileField(upload_to='FileRestore/static/css', default='none')
    js_address = models.FileField(upload_to='FileRestore/static/js', default='none')
    png_address = models.FileField(upload_to='FileRestore/static/png', default='none')


# python3 manage.py migrate --fake-initial重置数据库

class property(models.Model):
    userName = models.CharField(max_length=64)
    productName = models.CharField(max_length=64)
