from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# TODO: Create a mixins for all LoginRequiredMixin
class TeachersTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'teachers/index.html'
    login_url = reverse_lazy("accounts:accounts_login")
    redirect_field_name = "next_link"