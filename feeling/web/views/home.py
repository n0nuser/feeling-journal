from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought, Habit


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dates"] = {
            "journal": Journal.objects.filter(user=self.request.user).order_by("-ocurred_at").first().ocurred_at
            if Journal.objects.filter(user=self.request.user).exists()
            else None,
            "thought": Thought.objects.filter(user=self.request.user).order_by("-created_at").first().created_at
            if Thought.objects.filter(user=self.request.user).exists()
            else None,
            "habit": Habit.objects.filter(user=self.request.user).order_by("-ocurred_at").first().ocurred_at
            if Habit.objects.filter(user=self.request.user).exists()
            else None,
        }
        return context
