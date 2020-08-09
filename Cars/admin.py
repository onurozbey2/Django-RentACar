from django.contrib import admin
from cars.models import Cars, Images

# Register your models here.


class CarsImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'durum']
    list_filter = ['durum']
    inlines = [CarsImageInLine]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'cars', 'resim']


admin.site.register(Cars, CarsAdmin)
admin.site.register(Images, ImagesAdmin)
