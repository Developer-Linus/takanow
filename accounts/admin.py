from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('full_name', 'email', 'phone', 'role',
                    'location', 'is_active', 'is_staff',)
    list_filter = ('email', 'role', 'location', 'is_active', 'is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'phone', 'location', 'password',)}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff',)}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'phone', 'location', 'role', 'is_active', 'is_staff', 'groups', 'user_permissions',)}
         )
    )

    search_fields = ('email', 'phone', 'location', 'role',)
    ordering = ('email',)


admin.site.register(User, CustomAdmin)
