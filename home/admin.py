from django.contrib import admin
from home.models import Setting, ContactMessageForm
# Register your models here.


class ContactMessageFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'note', 'update_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


admin.site.register(Setting)
admin.site.register(ContactMessageForm, ContactMessageFormAdmin)
