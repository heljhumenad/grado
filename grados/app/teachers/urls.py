from django.urls import path

from grados.app.views import teachers

app_name = "teachers"

urlpatterns = [
    path("index/", teachers.TeachersTemplateView.as_view(), name="teachers_index"),
    path("add/", teachers.TeacherCreateView.as_view(), name="teachers_add"),
]
