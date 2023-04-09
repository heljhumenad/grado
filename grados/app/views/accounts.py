from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views

from grados.app.accounts.models import CustomUser
from grados.app.forms.accountsForm import CustomAuthenticationForm

class AccountTemplateView(views.LoginView):
    template_name = "accounts/login.html"
    form_class = CustomAuthenticationForm

class AccountLogoutView(LoginRequiredMixin, views.LogoutView):
    template_name = "accounts/logout.html"
    login_url = reverse_lazy("accounts:accounts_login")
    redirect_field_name = "next_link"


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("accounts:accounts_login")
    template_name = "accounts/dashboard.html"
    redirect_field_name = "next_link"
