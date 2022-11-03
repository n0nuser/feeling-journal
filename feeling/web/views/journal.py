from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Journal


@method_decorator(login_required, name="dispatch")
class JournalListView(ListView):
    model = Journal
    paginate_by: int = 10
    template_name: str = "journal/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("-ocurred_at")
        if search_value := self.request.GET.get("q"):
            q = q.filter(
                Q(situation_emotion__icontains=search_value)|Q(afterwards_feeling__icontains=search_value)
            )
        date_by = self.request.GET.get("date") or None
        times = {"week": 7, "midmonth": 15, "month": 30, "year": 365}
        if date_by in times:
            date_to = datetime.now().date()
            date_from = date_to - timedelta(days=times[date_by])
            q = q.filter(
                ocurred_at__gte=date_from,
                ocurred_at__lte=date_to,
            )

        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

@method_decorator(login_required, name="dispatch")
class JournalCreateView(CreateView):
    model = Journal
    form_class = forms.JournalForm
    success_url = reverse_lazy("journal_list")
    template_name = "common/add.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class JournalUpdateView(UpdateView):
    model = Journal
    form_class = forms.JournalForm
    success_url = reverse_lazy("journal_list")
    template_name = "common/edit.html"


@method_decorator(login_required, name="dispatch")
class JournalDeleteView(DeleteView):
    model = Journal
    success_url = reverse_lazy("journal_list")
    template_name = "common/delete.html"
