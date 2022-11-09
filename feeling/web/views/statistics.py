from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import ExtractWeekDay, ExtractHour
from django.db.models.query import QuerySet
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal


@method_decorator(login_required, name="dispatch")
class StatisticsView(TemplateView):
    template_name = "statistics/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if journal := Journal.objects.filter(user=self.request.user).order_by("ocurred_at"):
            date_by = self.request.GET.get("date") or None
            times = {"week": 7, "midmonth": 15, "month": 30, "year": 365}
            date_to = datetime.now().date()
            date_from = None
            if date_by in times:
                date_from = date_to - timedelta(days=times[date_by])
                journal = journal.filter(
                    ocurred_at__gte=date_from,
                    ocurred_at__lte=date_to,
                )

            context["actual_date"] = date_to
            context["origin_date"] = date_from
            context["journal"] = journal

            # Filling the missing days between entries
            fields = ["ocurred_at", "number_of_times"]
            date_field = 0  # index of the date field
            journal_filled = list(journal.values_list(*fields).order_by("ocurred_at"))
            first_date: datetime = journal_filled[0][date_field]  # first entry date
            last_date: datetime = journal_filled[-1][date_field]  # last entry date
            for i in range((last_date - first_date).days + 1):
                day = first_date + timedelta(days=i)
                day_zero = day.replace(hour=0, minute=0, second=0, microsecond=0)
                if all(
                    day_zero != (entry[date_field]).replace(hour=0, minute=0, second=0, microsecond=0)
                    for entry in journal_filled
                ):
                    journal_filled.append([day, 0])
            journal_filled.sort(key=lambda x: x[date_field])  # Sort by date
            js_datetime:str = lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
            context["journal_dates"] = [js_datetime(entry[date_field]) for entry in journal_filled]
            context["journal_values"] = [entry[1] for entry in journal_filled]

            # https://stackoverflow.com/a/40921159
            context["records_per_day"] = list(
                journal.filter().annotate(weekday=ExtractWeekDay("ocurred_at"))
                .values("weekday")
                .order_by("weekday")
                .annotate(count=Sum("number_of_times"))
                .values("weekday", "count")
            )

            context["records_per_hour"] = list(
                journal.annotate(hour=ExtractHour("ocurred_at"))
                .values("hour")
                .order_by("hour")
                .annotate(count=Sum("number_of_times"))
                .values("hour", "count")
            )

        return context
