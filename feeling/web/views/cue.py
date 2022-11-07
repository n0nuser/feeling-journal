from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Cue


@method_decorator(login_required, name="dispatch")
class CueListView(ListView):
    model = Cue
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("id", "general")
        if search_value := self.request.GET.get("q"):
            q = q.filter(trigger__icontains=search_value)
        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = False
        context["page_title"] = "Cues"
        context["create_url"] = "cue_create"
        context["update_url"] = "cue_update"
        context["delete_url"] = "cue_delete"
        context["columns"] = ["General", "Trigger"]
        context["object_fields"] = ["general", "trigger"]
        return context


@method_decorator(login_required, name="dispatch")
class CueCreateView(CreateView):
    model = Cue
    form_class = forms.CueForm
    success_url = reverse_lazy("cue_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class CueUpdateView(UpdateView):
    model = Cue
    form_class = forms.CueForm
    success_url = reverse_lazy("cue_list")
    template_name = "common/edit.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class CueDeleteView(DeleteView):
    model = Cue
    success_url = reverse_lazy("cue_list")
    template_name = "common/delete.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
