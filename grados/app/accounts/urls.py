from django.urls import path
from grados.app.views import accounts

app_name = "accounts"

urlpatterns = [
    path("login", accounts.AccountTemplateView.as_view(), name="account_view"),
    path("dashboard", accounts.DashboardTemplateView.as_view(), name="dashboard_view"),
]