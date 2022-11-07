from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Routine


@method_decorator(login_required, name="dispatch")
class RoutineListView(ListView):
    model = Routine
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("id", "general")
        if search_value := self.request.GET.get("q"):
            q = q.filter(response__icontains=search_value)
        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = False
        context["page_title"] = "Routines"
        context["create_url"] = "routine_create"
        context["update_url"] = "routine_update"
        context["delete_url"] = "routine_delete"
        context["columns"] = ["General", "Response"]
        context["object_fields"] = ["general", "response"]
        return context


@method_decorator(login_required, name="dispatch")
class RoutineCreateView(CreateView):
    model = Routine
    form_class = forms.RoutineForm
    success_url = reverse_lazy("routine_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class RoutineUpdateView(UpdateView):
    model = Routine
    form_class = forms.RoutineForm
    success_url = reverse_lazy("routine_list")
    template_name = "common/edit.html"


@method_decorator(login_required, name="dispatch")
class RoutineDeleteView(DeleteView):
    model = Routine
    success_url = reverse_lazy("routine_list")
    template_name = "common/delete.html"
