from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Add date_of_birth and profile_photo to the add fieldsets.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )

    # Specify the fields to display in the list view.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Add search functionality.
    search_fields = ('username', 'first_name', 'last_name', 'email')

    # Order the users by username.
    ordering = ('username',)

    # Add filter options.
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')


admin.site.register(CustomUser, CustomUserAdmin)

permissions = [
    Permission.objects.get_or_create(codename='can_view', name='Can view book', content_type=content_type),
    Permission.objects.get_or_create(codename='can_create', name='Can create book', content_type=content_type),
    Permission.objects.get_or_create(codename='can_edit', name='Can edit book', content_type=content_type),
    Permission.objects.get_or_create(codename='can_delete', name='Can delete book', content_type=content_type),
]

for perm, created in permissions:
    group.permissions.add(perm)
