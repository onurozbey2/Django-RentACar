# Generated by Django 3.0.8 on 2020-08-12 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200812_1638'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='ContactMessageForm',
        ),
    ]
