# Generated by Django 3.0.8 on 2020-08-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20200812_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]