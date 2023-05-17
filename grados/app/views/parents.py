from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from grados.app.forms.form import ParentForms
from grados.app.mixin.messagemixin import MessageMixins
from grados.app.parents.models import Parent

# TODO: Name standard for the template names for CRUD functionality


class ParentTemplateView(MessageMixins, TemplateView):
    template_name = "parents/index.html"


class ParentCreateView(MessageMixins, CreateView):
    template_name = "parents/add_parent.html"
    form_class = ParentForms
    success_url = reverse_lazy("parents:parent_index")
