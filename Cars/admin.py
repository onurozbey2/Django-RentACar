from django.contrib import admin
from cars.models import Cars, Images, Comment

# Register your models here.


class CarsImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'id', 'fiyat', 'model_yılı',
                    'motor_hacmi', 'yakıt', 'vites', 'image_tag', 'durum']
    list_filter = ['durum', 'yakıt', 'vites', 'kasa_tipi']
    inlines = [CarsImageInLine]
    readonly_fields = ['image_tag']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'cars', 'image_tag']
    readonly_fields = ['image_tag']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['car', 'comment', 'user', 'status']
    list_filter = ['status']


admin.site.register(Cars, CarsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
