from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Reward


@method_decorator(login_required, name="dispatch")
class RewardListView(ListView):
    model = Reward
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("id", "general")
        if search_value := self.request.GET.get("q"):
            q = q.filter(reward__icontains=search_value)
        return q

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = False
        context["page_title"] = "Rewards"
        context["create_url"] = "reward_create"
        context["update_url"] = "reward_update"
        context["delete_url"] = "reward_delete"
        context["columns"] = ["General", "Reward"]
        context["object_fields"] = ["general", "reward"]
        return context


@method_decorator(login_required, name="dispatch")
class RewardCreateView(CreateView):
    model = Reward
    form_class = forms.RewardForm
    success_url = reverse_lazy("reward_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class RewardUpdateView(UpdateView):
    model = Reward
    form_class = forms.RewardForm
    success_url = reverse_lazy("reward_list")
    template_name = "common/edit.html"


@method_decorator(login_required, name="dispatch")
class RewardDeleteView(DeleteView):
    model = Reward
    success_url = reverse_lazy("reward_list")
    template_name = "common/delete.html"
