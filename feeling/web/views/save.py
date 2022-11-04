from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought
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
    return PDF("journal", fields, 1, Journal, request.user, "journal/report-pdf.html")


@login_required
def ThoughtCSV(request):
    fields = ["id", "created_at", "journal", "thought"]
    return CSV("thought", fields, 1, Thought, request.user)


@login_required
def ThoughtPDF(request):
    fields = ["id", "created_at", "journal", "thought"]
    return PDF("journal", fields, 1, Thought, request.user, "journal/report-pdf.html")
