from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Thought
from web.views.utils import filter_date_by


@method_decorator(login_required, name="dispatch")
class ThoughtListView(ListView):
    model = Thought
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().select_related("journal").filter(user=self.request.user).order_by("-created_at")
        if search_value := self.request.GET.get("q"):
            q = q.filter(Q(situation_emotion__icontains=search_value) | Q(afterwards_feeling__icontains=search_value))
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(created_at__range=(date_to, date_from))
        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Thoughts"
        context["create_url"] = "thought_create"
        context["update_url"] = "thought_update"
        context["delete_url"] = "thought_delete"
        context["columns"] = ["Created At", "Associated Journal", "Thought"]
        context["object_fields"] = [
            "created_at",
            "journal__situation_emotion",
            "thought",
        ]
        return context


@method_decorator(login_required, name="dispatch")
class ThoughtCreateView(CreateView):
    model = Thought
    form_class = forms.ThoughtForm
    success_url = reverse_lazy("thought_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class ThoughtUpdateView(UpdateView):
    model = Thought
    form_class = forms.ThoughtForm
    success_url = reverse_lazy("thought_list")
    template_name = "common/edit.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class ThoughtDeleteView(DeleteView):
    model = Thought
    success_url = reverse_lazy("thought_list")
    template_name = "common/delete.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
