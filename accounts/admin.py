from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # List of fields to display in the change list page of the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'profile_image', 'address', 'phone_number')

    # Fields to include in the user edit form in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_image', 'address', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the ordering of fields in the user edit form
    # You can rearrange the order as needed
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# Register your custom admin class for the CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)
