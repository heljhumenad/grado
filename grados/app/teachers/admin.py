from django.contrib import admin

from grados.app.teachers.models import Teacher
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = [
        'birth_date',
        'teacher_accounts_id'
    ]

