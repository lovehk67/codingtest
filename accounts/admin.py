from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'address_new', 'phone', 'is_superuser')
    search_fields = ('username', 'email', 'address_new', 'address_old', 'address_input')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = ()

admin.site.register(User, AccountAdmin)
