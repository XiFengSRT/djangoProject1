# Generated by Django 3.1 on 2022-05-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='css_address',
            field=models.FileField(default='none', upload_to='uploadFile/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='html_address',
            field=models.FileField(default='none', upload_to='uploadFile/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='js_address',
            field=models.FileField(default='none', upload_to='uploadFile/'),
        ),
    ]
