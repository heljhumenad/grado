from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.accounts.models import CustomUser

class Teacher(models.Model, TimeStampModel):

    LIFE_DESIGNATION = (
        ('mr.', 'Mr.'),
        ('mrs.', 'Mrs.'),
        ('ms.', 'Miss')
    )

    teacher_accounts_id = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        verbose_name = _('Teacher Acccount')
    )

    address1 = models.CharField(
        max_length = 200,
        verbose_name = _('Address 1'),
        blank = False,
    )
    
    address2 = models.CharField(
        max_length = 200,
        verbose_name = _('Address 2'),
        blank = False,
    )

    birth_date = models.DateField(
        verbose_name = _('Birth Date'),
    )

    designation_as = models.CharField(
        choices = LIFE_DESIGNATION,
        max_length = 50,
        verbose_name = _('Designation As.'),

    )

    class Meta:
        db_table = _('teachers')
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ['id']

    def __str__(self):
        return f"{self.birth_date}"
