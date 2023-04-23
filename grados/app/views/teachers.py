from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    CreateView,
    UpdateView
)

from grados.app.teachers.models import Teacher
from grados.app.forms import teachers_form
from grados.app.mixin.messagemixin import MessageMixins

class TeachersTemplateView(MessageMixins, TemplateView):
    template_name = 'teachers/index.html'


class TeacherCreateView(MessageMixins, CreateView):
    template_name = 'teachers/add_teacher.html'
    form_class = teachers_form.TeacherForms
    field_name = "object.designation_as"
    messages = "added"
    success_url = reverse_lazy('teachers:teachers_add') # redirect and show messages

    # save the current logged-in user to the teacher model instance
    def form_valid(self, form):
        form.instance.teacher_accounts_id = self.request.user
        return super().form_valid(form)
    

class TeacherUpdateView(MessageMixins, UpdateView):
    pass