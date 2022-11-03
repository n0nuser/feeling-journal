from django.apps import apps
from django.contrib import admin
from web.models import Journal, Thought
from import_export.admin import ImportExportMixin

class JournalAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling")

class ThoughtAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('created_at', 'thought')

admin.site.register(Journal, JournalAdmin)
admin.site.register(Thought, ThoughtAdmin)