from django.contrib import admin
from cars.models import Cars, Images

# Register your models here.


class CarsImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'fiyat', 'model_yılı', 'motor_hacmi', 'vites', 'image_tag', 'durum']
    list_filter = ['durum']
    inlines = [CarsImageInLine]
    readonly_fields = ['image_tag']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'cars', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Cars, CarsAdmin)
admin.site.register(Images, ImagesAdmin)
