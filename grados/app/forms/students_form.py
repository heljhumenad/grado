from django import forms
from django.utils.translation import gettext as _

from grados.app.students.models import Student
from grados.app.teacher.models import Teacher
from grados.app.configs.settings.grados_settings import MAX_AGE_LIMIT

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

    def clean_age(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')

        if int(age) <= MAX_AGE_LIMIT:
            raise forms.ValidationError(
                _('Age of %(age)s is not allowed to use'),
                params = {'age': age},
        )
        return age
