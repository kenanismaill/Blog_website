from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, userProfile


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'note', 'status', 'ip']
    list_filter = ['status']


class userProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag','phone','country']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(userProfile, userProfileAdmin)
