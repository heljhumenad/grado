from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, TemplateView

# TODO: make this standard importing for forms
from grados.app.forms.form import StudentForm
from grados.app.mixin.messagemixin import MessageMixins
from grados.app.students.models import Student


class StudentsTemplateView(TemplateView):
    template_name = "students/index.html"


# TODO: add the student urls
class StudentCreateView(MessageMixins, CreateView):
    template_name = "students/student_add.html"
    form_class = StudentForm
    message = "added"
    success_url = reverse_lazy("student:students_index")
