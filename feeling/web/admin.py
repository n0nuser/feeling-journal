from django.apps import apps
from django.contrib import admin
from web.models import Journal, Thought, Habit, Cue, Routine, Reward
from import_export.admin import ImportExportMixin


class JournalAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("ocurred_at", "user", "number_of_times", "situation_emotion", "afterwards_feeling")
    list_filter = ("ocurred_at", "user", "number_of_times")


class ThoughtAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("created_at", "user", "thought")
    list_filter = ("created_at", "user")


class HabitAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("created_at", "ocurred_at", "user", "number_of_times", "cue", "routine", "reward")
    list_filter = ("created_at", "ocurred_at", "user", "number_of_times", "cue", "routine", "reward")


class CueAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("user", "trigger", "general")
    list_filter = ("user", "general")


class RoutineAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("user", "response", "general")
    list_filter = ("user", "general")


class RewardAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("user", "reward", "general")
    list_filter = ("user", "general")


admin.site.register(Journal, JournalAdmin)
admin.site.register(Thought, ThoughtAdmin)
admin.site.register(Habit, HabitAdmin)
admin.site.register(Cue, CueAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.site_header = "Feeling"
admin.site.site_title = "Feeling"
