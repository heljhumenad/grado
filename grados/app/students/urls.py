from django.urls import path

from grados.app.views import students

app_name = "students"


urlpatterns = [
    path("index/", students.StudentsTemplateView.as_view(), name="students_index"),
    path("add/", students.StudentCreateView.as_view(), name="student_add"),
]
