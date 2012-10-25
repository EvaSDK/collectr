from django.contrib import admin

from userprofile import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']

admin.site.register(models.UserProfile, UserProfileAdmin)

