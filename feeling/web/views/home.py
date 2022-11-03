from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponse


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "index.html"
