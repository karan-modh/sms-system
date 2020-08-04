from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'company_name', 'date_joined', 'is_admin')
    search_fields = ('pk', 'email', 'username',)
    readonly_fields = ('pk', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
