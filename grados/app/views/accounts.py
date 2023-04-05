from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from grados.app.accounts.models import CustomUser



class AccountTemplateView(views.LoginView):
    template_name = "accounts/login.html"

class DashboardTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/dashboard.html"