from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.teachers.models import Teacher

# TODO: Create normalize table for students and teacher
class Student(models.Model, TimeStampModel):
    
    teacher_id = models.ForeignKey(
        Teacher,
        on_delete = models.CASCADE,
        verbose_name = _('Students')
    )

    first_name = models.CharField(
        max_length = 200,
        verbose_name = _('First Name'),
        blank = False
    )

    last_name = models.CharField(
        max_length = 200,
        verbose_name = _('Last Name'),
        blank = False
    )

    middle_name = models.CharField(
        max_length = 200,
        verbose_name = _('Middle Name'),
        blank = False
    )
    
    age = models.SmallIntegerField(
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
    

