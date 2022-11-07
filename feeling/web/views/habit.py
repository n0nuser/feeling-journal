from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Habit, Cue, Routine, Reward
from web.views.utils import filter_date_by, filter_by_model


@method_decorator(login_required, name="dispatch")
class HabitListView(ListView):
    model = Habit
    paginate_by: int = 10
    template_name: str = "habit/list.html"

    def get_queryset(self):
        q = (
            super()
            .get_queryset()
            .select_related("cue", "routine", "reward")
            .filter(user=self.request.user)
            .order_by("-ocurred_at")
        )
        if search_value := self.request.GET.get("q"):
            q = q.filter(
                Q(cue__trigger__icontains=search_value)
                | Q(routine__response__icontains=search_value)
                | Q(reward__reward__icontains=search_value)
            )
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(ocurred_at__range=(date_to, date_from))
        q = filter_by_model(self.request, "cue", Cue, "cue", q)
        q = filter_by_model(self.request, "routine", Routine, "routine", q)
        q = filter_by_model(self.request, "reward", Reward, "reward", q)
        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Habits"
        context["create_url"] = "habit_create"
        context["update_url"] = "habit_update"
        context["delete_url"] = "habit_delete"
        context["columns"] = ["Ocurred at", "Number of times", "Cue", "Routine", "Reward"]
        context["object_fields"] = [
            "ocurred_at",
            "number_of_times",
            "cue__trigger",
            "routine__response",
            "reward__reward",
        ]
        context["cue"] = Cue.objects.filter(user=self.request.user)
        context["routine"] = Routine.objects.filter(user=self.request.user)
        context["reward"] = Reward.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name="dispatch")
class HabitCreateView(CreateView):
    model = Habit
    form_class = forms.HabitForm
    success_url = reverse_lazy("habit_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class HabitUpdateView(UpdateView):
    model = Habit
    form_class = forms.HabitForm
    success_url = reverse_lazy("habit_list")
    template_name = "common/edit.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class HabitDeleteView(DeleteView):
    model = Habit
    success_url = reverse_lazy("habit_list")
    template_name = "common/delete.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
