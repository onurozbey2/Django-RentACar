# Generated by Django 3.0.8 on 2020-08-21 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_remove_reservation_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='message',
        ),
    ]
