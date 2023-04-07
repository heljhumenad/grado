from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from grados.app.accounts.models import CustomUser



class AccountTemplateView(views.LoginView):
    template_name = "accounts/login.html"

class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "accounts/dashboard.html"
    redirect_field_name = "next_link"
