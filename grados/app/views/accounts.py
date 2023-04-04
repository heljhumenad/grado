from django.views.generic import TemplateView


class AccountTemplateView(TemplateView):
    template_name = "accounts/index.html"