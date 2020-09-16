from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'address_new', 'phone', 'is_superuser')
    search_fields = ('username', 'email', 'address_new', 'address_old', 'address_input')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'email', 'address_input', 'address_new', 'address_old', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('username', 'email', 'password1', 'password2', 'address_input', 'phone')
        }),
    )


admin.site.register(User, AccountAdmin)
