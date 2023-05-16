from django.db import models
from django.utils.translation import gettext as _

from grados.app.accounts.models import CustomUser
from grados.app.core.models import TimeStampModel

# Create your models here.

class StudentClass(models.Model, TimeStampModel):
    
    class_name = models.CharField(
        max_length = 200,
        verbose_name = _('Name of Class'),
        blank = False
    )

    class_sched = models.DateTimeField(
        verbose_name = _('Schedule of class')
    )

    class_desc = models.CharField(
        max_length = 200,
        verbose_name = _('Description of Class')
    )

    max_students_enrolled = models.CharField(
        max_length = 200,
        verbose_name = _('Students Enrolled in Class'),
        blank = False,
    )

    class_status = models.CharField(
        max_length = 200,
        verbose_name = _('Status of Class'),
        blank = False
    )
    # TODO: Add logic for step wizard when dealing the approved and editing of a student class
    approved_by = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        verbose_name = _('Approved By'),
    )

    updated_by = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        verbose_name = _('Updated By')
    )

    class Meta:
        db_table = _('student_class')
        verbose_name = _('Students Class')
        verbose_name_plural = _('Student Classes')
        ordering = ['id']

