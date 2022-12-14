from core import settings
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import csv
import os


def rangeDate(request, hours: int = None, days: int = None, weeks: int = None):
    startDate = request.GET.get("start")
    endDate = request.GET.get("end")

    date_to = date_from = None
    if startDate and endDate:
        date_from = datetime.strptime(startDate, "%Y-%m-%d")
        date_to = datetime.strptime(endDate, "%Y-%m-%d")
    if startDate and not endDate:
        date_from = datetime.strptime(startDate, "%Y-%m-%d")
        date_to = datetime.now()
    if date_to and date_from:
        return date_from, date_to

    if hours:
        date_from = datetime.now() - timedelta(hours=hours)
    elif days:
        date_from = datetime.now() - timedelta(days=days)
    elif weeks:
        date_from = datetime.now() - timedelta(weeks=weeks)
    date_to = datetime.now()
    return date_from, date_to


def filter_date_by(request):
    date_by = request.GET.get("date") or None
    times = {"week": 7, "midmonth": 15, "month": 30, "year": 365}
    date_to = date_from = None
    if date_by in times:
        date_to = datetime.now().date()
        date_from = date_to - timedelta(days=times[date_by])
    return date_to, date_from


def filter_by_model(request, request_name_value, model, fk, q):
    filter_field = request.GET.get(request_name_value) or None
    if filter_field == 0:
        return q
    model = model.objects.filter(id=filter_field).first()
    if filter_field and model:
        args = {fk: model}
        q = q.filter(**args)
    return q


def get_model_date_filled(fields: list = None, date_field_index: int = 0, model=None, user=None) -> list:
    if fields is None:
        fields = []
    query = list(model.objects.filter(user=user).values_list(*fields).order_by(fields[date_field_index]))

    # Filling the missing days between entries
    first_date = query[0][date_field_index]  # first entry date
    last_date = query[-1][date_field_index]  # last entry date
    for i in range((last_date - first_date).days + 1):
        day = (first_date + timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        if all(day != (entry[date_field_index]).replace(hour=0, minute=0, second=0, microsecond=0) for entry in query):
            query.append([None, day, None, None])

    query.sort(key=lambda x: x[date_field_index])  # Sort by date
    return query


def PDF(
    filename: str = None,
    fields: list = None,
    date_field_index: int = 0,
    is_date_filled: bool = False,
    model=None,
    user=None,
    template_html: str = None,
) -> HttpResponse:
    if not model.objects.filter(user=user).exists():
        return HttpResponse("No data available")

    if is_date_filled:
        context = {"model": get_model_date_filled(fields, date_field_index, model, user)}
    else:
        context = {"model": list(model.objects.filter(user=user).values_list(*fields))}
    date_now = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")

    font_config = FontConfiguration()  # Install fonts in the system
    css = CSS(os.path.join(settings.BASE_DIR, "static/css/report-pdf.css"), font_config=font_config)
    html = render_to_string(template_html, context)
    html_weasyprint = HTML(string=html)
    pdf = html_weasyprint.write_pdf(stylesheets=[css])

    response = HttpResponse(pdf)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'inline; filename="{filename}--{date_now}.pdf"'
    return response


def CSV(
    filename: str = None,
    fields: list = None,
    date_field_index: int = 0,
    is_date_filled: bool = False,
    model=None,
    user=None,
) -> HttpResponse:
    if not model.objects.filter(user=user).exists():
        return HttpResponse("No data available")

    date_now = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}--{date_now}.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(fields)  # Write header row
    if is_date_filled:
        model_altered = get_model_date_filled(fields, date_field_index, model, user)
    else:
        model_altered = list(model.objects.filter(user=user).values_list(*fields))
    writer.writerows(model_altered)  # Write data rows
    return response
