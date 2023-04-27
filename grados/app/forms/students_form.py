from django import forms
from django.utils.translation import gettext as _

from grados.app.students.models import Student


# TODO: Add models for students and create normalize table from it
class StudentsForm(forms.ModelForm):
    class Meta:
        verbose_name = _('Students Form')
        verbose_plural_name = _('Teachers Forms')
        model = Student
