from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','mobile','email','avatar']
    list_display_links = ['username']
    list_filter = ['id','username','mobile','email']
    search_fields = ['username','email','mobile']
    list_editable = ['email','mobile']

admin.site.register(User,UserAdmin)
