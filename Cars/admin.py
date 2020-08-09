from django.contrib import admin
from cars.models import Cars

# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'durum']
    list_filter = ['durum']


admin.site.register(Cars, CarsAdmin)
