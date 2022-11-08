from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought, Cue, Routine, Reward, Habit
from web.views.utils import CSV, PDF


@method_decorator(login_required, name="dispatch")
class SaveView(TemplateView):
    template_name = "save/index.html"


@login_required
def JournalCSV(request):
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    return CSV("journal", fields, 1, Journal, request.user)


@login_required
def JournalPDF(request):
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    return PDF("journal", fields, 1, Journal, request.user, "journal/report-pdf.html", True)


@login_required
def ThoughtCSV(request):
    fields = ["id", "created_at", "journal", "thought"]
    return CSV("thought", fields, 1, Thought, request.user)


@login_required
def ThoughtPDF(request):
    fields = ["id", "created_at", "journal", "thought"]
    return PDF("journal", fields, 1, Thought, request.user, "thought/report-pdf.html", True)


@login_required
def CueCSV(request):
    fields = ["id", "trigger"]
    return CSV("cue", fields, 1, Cue, request.user)


@login_required
def CuePDF(request):
    fields = ["id", "trigger"]
    return PDF("cue", fields, 1, Cue, request.user, "cue/report-pdf.html", False)


@login_required
def RoutineCSV(request):
    fields = ["id", "type", "response"]
    return CSV("routine", fields, 1, Routine, request.user)


@login_required
def RoutinePDF(request):
    fields = ["id", "type", "response"]
    return PDF("routine", fields, 1, Routine, request.user, "routine/report-pdf.html", False)


@login_required
def RewardCSV(request):
    fields = ["id", "reward"]
    return CSV("reward", fields, 1, Reward, request.user)


@login_required
def RewardPDF(request):
    fields = ["id", "reward"]
    return PDF("reward", fields, 1, Reward, request.user, "reward/report-pdf.html", False)


@login_required
def HabitCSV(request):
    fields = ["id", "ocurred_at", "number_of_times", "cue", "routine", "reward"]
    return CSV("habit", fields, 1, Habit, request.user)


@login_required
def HabitPDF(request):
    fields = ["id", "ocurred_at", "number_of_times", "cue", "routine", "reward"]
    return PDF("habit", fields, 1, Habit, request.user, "habit/report-pdf.html", True)
