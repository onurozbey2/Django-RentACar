# Generated by Django 3.0.8 on 2020-08-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_auto_20200817_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
