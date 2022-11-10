from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import ExtractWeekDay, ExtractHour
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought, Habit
from web.views.utils import filter_date_by

js_datetime: str = lambda x: x.strftime("%Y-%m-%d %H:%M:%S")


@method_decorator(login_required, name="dispatch")
class StatisticsView(TemplateView):
    template_name = "statistics/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["summary"] = {}
        date_to, date_from = filter_date_by(self.request)

        if date_to and date_from:
                journal = Journal.objects.filter(user=self.request.user).order_by("ocurred_at").filter(ocurred_at__range=(date_from, date_to))
                thought = Thought.objects.filter(user=self.request.user).order_by("created_at").filter(created_at__range=(date_from, date_to))
                habit = Habit.objects.filter(user=self.request.user).order_by("ocurred_at").filter(ocurred_at__range=(date_from, date_to))
        else:
            journal = Journal.objects.filter(user=self.request.user).order_by("ocurred_at")
            thought = Thought.objects.filter(user=self.request.user).order_by("created_at")
            habit = Habit.objects.filter(user=self.request.user).order_by("ocurred_at")
        
        if journal:
            context["actual_date"] = date_to
            context["origin_date"] = date_from
            context["journal"] = journal

            # Filling the missing days between entries
            if journal_filled := fill_model_with_dates(journal, ["ocurred_at", "number_of_times"], 0):
                context["journal_dates"] = [js_datetime(entry[0]) for entry in journal_filled]
                context["journal_values"] = [entry[1] for entry in journal_filled]

            # https://stackoverflow.com/a/40921159
            context["records_per_day"] = list(records_per_day(journal, "ocurred_at", "number_of_times"))
            context["records_per_hour"] = list(records_per_hour(journal, "ocurred_at", "number_of_times"))

            context["summary"] = {
                "journal": {
                    "weekday_mode": mode_of_records_per_weekday(journal, "ocurred_at", "number_of_times"),
                    "hour_mode": mode_of_records_per_hour(journal, "ocurred_at", "number_of_times"),
                }
            }

        if thought:
            context["summary"]["thought"] = {
                "weekday_mode": mode_of_records_per_weekday(thought, "created_at", "id"),
                "hour_mode": mode_of_records_per_hour(thought, "created_at", "id"),
            }

        if habit:
            context["summary"]["habit"] = {
                "weekday_mode": mode_of_records_per_weekday(habit, "ocurred_at", "number_of_times"),
                "hour_mode": mode_of_records_per_hour(habit, "ocurred_at", "number_of_times"),
            }

        return context


def fill_model_with_dates(model, fields, date_field):
    model_filled = list(model.values_list(*fields).order_by(fields[date_field]))
    if not model_filled:
        return None
    first_date: datetime = model_filled[0][date_field]  # first entry date
    last_date: datetime = model_filled[-1][date_field]  # last entry date
    for i in range((last_date - first_date).days + 1):
        day = first_date + timedelta(days=i)
        day_zero = day.replace(hour=0, minute=0, second=0, microsecond=0)
        if all(
            day_zero != (entry[date_field]).replace(hour=0, minute=0, second=0, microsecond=0)
            for entry in model_filled
        ):
            model_filled.append([day, 0])
    model_filled.sort(key=lambda x: x[date_field])  # Sort by date
    return model_filled


def records_per_day(model, date_field: str = "ocurred_at", value_field: str = "number_of_times"):
    return (
        model.annotate(weekday=ExtractWeekDay(date_field))
        .values("weekday")
        .order_by("weekday")
        .annotate(count=Sum(value_field))
    )


def records_per_hour(model, date_field: str = "ocurred_at", value_field: str = "number_of_times"):
    return (
        model.annotate(hour=ExtractHour(date_field)).values("hour").order_by("hour").annotate(count=Sum(value_field))
    )


def mode_of_records_per_weekday(model, date_field: str = "ocurred_at", value_field: str = "number_of_times"):
    return records_per_day(model, date_field, value_field).order_by("-count").first()


def mode_of_records_per_hour(model, date_field: str = "ocurred_at", value_field: str = "number_of_times"):
    return records_per_hour(model, date_field, value_field).order_by("-count").first()
