from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from grados.app.teachers.models import Teacher
from grados.app.forms import teachers_form

# TODO: Create a mixins for all LoginRequiredMixin
class TeachersTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'teachers/index.html'
    login_url = reverse_lazy("accounts:accounts_login")
    redirect_field_name = "next_link"

class TeacherCreateView(LoginRequiredMixin, CreateView):
    template_name = 'teachers/add_teacher.html'
    form_class = teachers_form.TeacherForms
    success_url = reverse_lazy('teachers:teachers_index')
    login_url = reverse_lazy('accounts:accounts_login')

    # save the current logged-in user to the teacher model instance
    def form_valid(self, form):
        form.instance.teacher_accounts_id = self.request.user
        return super().form_valid(form)
