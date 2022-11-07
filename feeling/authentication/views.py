from authentication.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, TemplateView, CreateView

from authentication import models, forms


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")
    form_class = SignUpForm
    success_message = "Your profile was created successfully"


class ProfileTemplateView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        " If you don't receive an email, "
        "please make sure you've entered the address you registered with, and check your spam folder."
    )
    success_url = reverse_lazy("login")


class ResetPasswordConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_message = "Your password has been reset. You can now log in."
    success_url = reverse_lazy("login")


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
    success_message = "Your password has been reset. You can now log in."
    success_url = reverse_lazy("login")


@method_decorator(login_required, name="dispatch")
class UpdateProfile(UpdateView):
    model = models.CustomUser
    form_class = forms.CustomUserForm
    template_name = "common/edit.html"
    success_url = reverse_lazy("profile")


@method_decorator(login_required, name="dispatch")
class PasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("profile")


def handler403(request, exception, template_name="errors/403.html"):
    return render(request, template_name, status=403)


def handler404(request, exception, template_name="errors/404.html"):
    return render(request, template_name, status=404)


def handler500(request, template_name="errors/500.html"):
    return render(request, template_name, status=500)
