from django.utils.translation import gettext as _
from djang.urls import reverse_lazy
from django.views.generic import (
    TemplateView
)

from grados.app.students.models import Student
from grados.app.mixin.messagemixin import MessageMixins
from grados.app.forms.student_form import


class StudentsTemplateView(TemplateView):
    template_name = 'students/index.html'

# TODO: add the student urls
class StudentCreateView(MessageMixins, CreateView):
    template_name = 'students/student_add.html'
    form_class = students_form.StudentForm
    message = 'added'
    success_url = reverse_lazy('student:students_index')

