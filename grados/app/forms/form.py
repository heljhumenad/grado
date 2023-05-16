from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

from grados.app.parents.models import Parent
from grados.app.students.models import Student
from grados.app.teachers.models import Teacher
from grados.configs.settings.grados_settings import MAX_AGE_LIMIT


class FormsForm(forms.ModelForm):
    '''
        Base form class that will be use to add global functionality
        of the ModelForm classes
    '''
    pass


class CustomAuthenticationForm(AuthenticationForm):
	error_messages = {
		"invalid_login": "Username and Password doesnt recognize by the system",
		"inactive": "Permission denied",
	}
	# BUG: when submitting the form non field error resetting the form
	def __init__(self, *args, **kwargs):	
		super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
		self.fields['username'].error_messages = {'required': "Username is required field"}
		self.fields['password'].error_messages = {'required': "Password is required field"}
                

class TeacherForms(FormsForm):
    class Meta:
        verbose_name = _('Teacher Form')
        verbose_plural_name = _('Teachers Forms')
        model = Teacher
        fields = [
            'address1', 'address2', 'birth_date', 'designation_as', 'role_of_work',
            'teacher_status', 'profile_pic_id'
        ]
        ordering = ['-id']


class ParentForms(FormsForm):
    class Meta:
        verbose_name = _('Parent Form')
        verbose_plural_name = _('Parents Forms')
        model = Parent
        fields = [
            'student_id', 'first_name', 'last_name', 'middle_name','occupation', 
            'address1', 'address2', 'tel_number','phone_number', 'email_address',
            'legal_guardian'
        ]
        ordering = ['id']


class StudentForm(FormsForm):
    teacher_id = forms.ModelChoiceField(
        queryset =  Teacher.objects.order_by('teacher_accounts_id'),
        empty_label = _('Choose Teacher')
    )

    class Meta:
        verbose_name = _('Student Form')
        verbose_plural_name = _('Students Forms')
        model = Student
        fields = [
            'teacher_id', 'first_name', 'last_name', 'middle_name', 'age'
        ]
        ordering = ['-id']

    def clean_age(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')

        if int(age) <= MAX_AGE_LIMIT:
            raise forms.ValidationError(
                _('Age of %(age)s is not allowde to use'),
                params = {'age': age},
            )
        return age