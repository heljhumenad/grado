from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import GradoBasicInfo, GradoTimeStampModel
from grados.app.teachers.models import Teacher


# TODO: Create normalize table for students and teacher
class Student(GradoBasicInfo, GradoTimeStampModel):
    teacher_id = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name=_("Students")
    )

    age = models.SmallIntegerField(verbose_name=_("Age"), blank=False)

    class Meta:
        db_table = _("students")
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ["id"]

    def __str__(self):
        return f"{self.stud_firstname} {self.stud_lastname}"
