from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class LoginRequiredMixins(LoginRequiredMixin):
    redirect_field_name = 'next_link'
    login_url = reverse_lazy('accounts:accounts_login')

