from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from authentication import views

urlpatterns = [
    path("accounts/login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("accounts/register/", views.SignUpView.as_view(), name="register"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/profile/", views.ProfileTemplateView.as_view(), name="profile"),
    path("accounts/update_profile/<pk>", views.UpdateProfile.as_view(), name="update-profile"),
    path("password-reset/", views.ResetPasswordView.as_view(), name="password-reset"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.ResetPasswordConfirmView.as_view(),
        name="password-reset-confirm",
    ),
    path("password-reset-complete/", views.PasswordResetCompleteView.as_view(), name="password-reset-complete"),
    path("change-password/", views.PasswordChangeView.as_view(), name="change-password"),
]
