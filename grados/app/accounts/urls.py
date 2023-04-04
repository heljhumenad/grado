from django.urls import path
from grados.app.views import accounts

# app_name = "accounts"

urlpatterns = [
    path("dashboard", accounts.AccountTemplateView.as_view(), name="account_view"),
]