# Generated by Django 3.0.8 on 2020-08-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
