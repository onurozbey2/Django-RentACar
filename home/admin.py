from django.contrib import admin
from home.models import Setting, ContactMessageForm, UserProfile
# Register your models here.


class ContactMessageFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'note', 'update_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'image_tag']


admin.site.register(Setting)
admin.site.register(ContactMessageForm, ContactMessageFormAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
