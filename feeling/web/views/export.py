from core import settings
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import csv
import os

from web.models import Journal, Thought

@method_decorator(login_required, name="dispatch")
class ExportView(TemplateView):
    template_name = "export/index.html"

def get_journal_date_filled(request):
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    date_field = 1
    journal = list(
        Journal.objects
        .filter(user=request.user)
        .values_list(*fields)
        .order_by("ocurred_at")
    )

    # Filling the missing days between entries
    first_date: datetime = journal[0][date_field]  # first entry date
    last_date: datetime = journal[-1][date_field]  # last entry date
    for i in range((last_date - first_date).days + 1):
        day = (first_date + timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        if all(day != (entry[date_field]).replace(hour=0, minute=0, second=0, microsecond=0) for entry in journal):
            journal.append([None, day, 0, None, None])
    
    journal.sort(key=lambda x: x[date_field])  # Sort by date
    return journal

def get_thoughts_date_filled(request):
    fields = ["id", "created_at", "journal", "thought"]
    date_field = 1  # index of the date field
    thoughts = list(
        Thought.objects
        .select_related("journal")
        .filter(user=request.user)
        .values_list(*fields)
        .order_by("created_at")
    )

    # Filling the missing days between entries
    first_date = thoughts[0][date_field]  # first entry date
    last_date = thoughts[-1][date_field]  # last entry date
    for i in range((last_date - first_date).days + 1):
        day = (first_date + timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        if all(day != (entry[date_field]).replace(hour=0, minute=0, second=0, microsecond=0) for entry in thoughts):
            thoughts.append([None, day, None, None])
    
    thoughts.sort(key=lambda x: x[date_field])  # Sort by date
    return thoughts

@login_required
def JournalCSV(request):
    journal_date = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="journal--{journal_date}.csv"'},
    )
    writer = csv.writer(response)
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    writer.writerow(fields)  # Write header row
    
    journal = get_journal_date_filled(request)
    writer.writerows(journal)  # Write data rows
    return response


@login_required
def ThoughtCSV(request):
    thought_date = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="thought--{thought_date}.csv"'},
    )
    writer = csv.writer(response)
    fields = ["id", "created_at", "journal", "thought"]
    writer.writerow(fields)  # Write header row
    
    thoughts = get_thoughts_date_filled(request)
    writer.writerows(thoughts)  # Write data rows
    return response

@login_required
def JournalPDF(request):
    context = {"journal": get_journal_date_filled(request)}
    journal_date = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    
    font_config = FontConfiguration()  # Install fonts in the system
    css = CSS(os.path.join(settings.BASE_DIR, 'static/css/report-pdf.css'), font_config=font_config)
    html = render_to_string("journal/report-pdf.html", context)
    html_weasyprint = HTML(string=html)
    pdf = html_weasyprint.write_pdf(stylesheets=[css])
    
    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'inline; filename="journal--{journal_date}.pdf"'

    return response

@login_required
def ThoughtPDF(request):
    context = {"thought": get_thoughts_date_filled(request)}
    thought_date = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    
    font_config = FontConfiguration()  # Install fonts in the system
    css = CSS(os.path.join(settings.BASE_DIR, 'static/css/report-pdf.css'), font_config=font_config)
    html = render_to_string("thought/report-pdf.html", context)
    html_weasyprint = HTML(string=html)
    pdf = html_weasyprint.write_pdf(stylesheets=[css])
    
    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'inline; filename="thought--{thought_date}.pdf"'

    return response
