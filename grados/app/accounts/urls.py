from django.urls import path

from grados.app.views import accounts

app_name = "accounts"

urlpatterns = [
    path("login", accounts.AccountTemplateView.as_view(), name="accounts_login"),
    path("logout", accounts.AccountLogoutView.as_view(), name="accounts_logout"),
    path("dashboard", accounts.DashboardTemplateView.as_view(), name="dashboard_view"),
]
