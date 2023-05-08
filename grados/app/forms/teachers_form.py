from django import forms
from django.utils.translation import gettext as _

from grados.app.teachers.models import Teacher


class TeacherForms(forms.ModelForm):
    class Meta:
        verbose_name = _('Teacher Form')
        verbose_plural_name = _('Teachers Forms')
        model = Teacher
        fields = [
            'address1',
            'address2',
            'birth_date',
            'designation_as',
            'role_of_work',
            'teacher_status',
            'profile_pic_id',
        ]
        ordering = ['-id']
    
