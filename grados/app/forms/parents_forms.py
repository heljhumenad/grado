from django import forms
from django.utils.translation import gettext as _

from grados.app.parents.models import Parent


class ParentForms(forms.ModelForm):
    class Meta:
        verbose_name = _('Parent Form')
        verbose_plural_name = _('Parents Forms')
        model = Parent
        fields = [
            'student_id',
            'first_name',
            'last_name',
            'middle_name',
            'occupation',
            'address1',
            'address2',
            'tel_number',
            'phone_number',
            'email_address',
            'legal_guardian',
        ]
        ordering = ['-id']