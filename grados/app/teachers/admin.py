from django.contrib import admin

from grados.app.teachers.models import Teacher
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = [
        'first_name', 'last_name', 'birth_date'
    ]

