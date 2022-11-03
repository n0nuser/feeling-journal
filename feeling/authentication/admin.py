from django.apps import apps
from django.contrib import admin
from authentication.models import CustomUser
from import_export.admin import ImportExportMixin

class CustomUserAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')

admin.site.register(CustomUser, CustomUserAdmin)