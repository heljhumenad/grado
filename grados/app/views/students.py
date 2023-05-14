from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView
)

from grados.app.students.models import Student
from grados.app.mixin.messagemixin import MessageMixins
# TODO: make this standard importing for forms
from grados.app.forms.form import StudentsForm


class StudentsTemplateView(TemplateView):
    template_name = 'students/index.html'

# TODO: add the student urls
class StudentCreateView(MessageMixins, CreateView):
    template_name = 'students/student_add.html'
    form_class = StudentsForm
    message = 'added'
    success_url = reverse_lazy('student:students_index')

