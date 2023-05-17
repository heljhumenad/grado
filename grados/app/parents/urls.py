from django.urls import path

from grados.app.views import parents

app_name = "parents"

urlpatterns = [
    path("", parents.ParentTemplateView.as_view(), name="parents_index"),
    path("add/", parents.ParentCreateView.as_view(), name="parents_add"),
]
