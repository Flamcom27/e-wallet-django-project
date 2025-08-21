from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ImageTest

# Register your models here.
class CustomUserAdmin(UserAdmin):
        fieldsets = list(UserAdmin.fieldsets)
        fieldsets[0] = (None, {'fields': ('username', 'password', 'icon')})
        UserAdmin.fieldsets = tuple(fieldsets)

admin.site.register(User, CustomUserAdmin)
admin.site.register(ImageTest)
