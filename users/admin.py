from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Photo

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'email', 'profile_picture', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('profile_picture',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Photo)