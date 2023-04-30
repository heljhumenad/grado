from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.teachers.models import Teacher
from grados.app.parents.models import Parent

# TODO: Create normalize table for students and teacher
class Student(model.Model, TimeStampModel):
    
    teacher_id = models.ForeignKey(
        Teacher,
        on_delete = models.CASCADE,
        verbose_name = _('Students')
    )
    
    parent_id = models.ForeignKey(
        Parent,
        on_delete = models.CASCADE,
        verbose_name = _('Parents')
    )

    age = models.SmallIntegerField(
        max_length = 100,
        verbose_name = _('Age'),
        blank = False
    )

    
            
    class Meta:
        db_table = _('students')
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ['id']

    def __str__(self):
        return f"{self.stud_firstname} {self.stud_lastname}"
    

