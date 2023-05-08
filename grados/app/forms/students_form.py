from django import forms
from django.utils.translation import gettext as _

from grados.app.students.models import Student
from grados.app.teacher.models import Teacher


# TODO: Add models for students and create normalize table from it
class StudentsForm(forms.ModelForm):

    teacher_id = forms.ModelChoiceField(
        queryset = Teacher.objects.order_by("teacher_accounts_id"),
        empty_label = _('Choose Teacher'),   
    )

    class Meta:
        verbose_name = _('Students Form')
        verbose_plural_name = _('Teachers Forms')
        model = Student
        fields = [
            'teacher_id',
            'first_name',
            'last_name',
            'middle_name',
            'age'
        ]
        ordering = ['-id']
