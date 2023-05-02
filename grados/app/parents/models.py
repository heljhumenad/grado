from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.accounts.models import CustomUser
from grados.app.students.models import Student


class Parent(models.Model, TimeStampModel):

    student_id = models.ForeignKey(
        Students,
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

    occupation = models.CharField(
        max_length = 200,
        verbose_name = _('Occupation'),
        blank = False
    )

    address1 = models.CharField(
        max_length = 200,
        verbose_name = _('Address 1')
        blank = False
    )

    address2 = models.CharField(
        max_length = 200,
        verbose_name = _('Address 2')
        blank = False
    )

    tel_number = models.CharField(
        max_length = 20,
        verbose_name = _('Telephone Number'),
        blank = True
    )

    phone_number = models.CharField(
        max_length = 20,
        verbose_name = _('Phone Number'),
        blank = True
    )

    emaill_address = models.CharField(
        max_length = 200,
        verbose_name = _('Email Address'),
        blank = False
    )
    # TODO: Check if this field is need to be Boolean Field 
    # TODO: What will be the design if the user will pick No as Legal Guardian
    legal_guardian = models.CharField(
        max_length = 10,
        verbose_name = _('Legal Guardian'),
        blank = False
    )


    class Meta:
        db_table = _('parents')
        verbose_name = _('Parent')
        verbose_name_plural = _('Parents')
        ordering = ['id']

    def __str__(self):
        return f"{self.parent_firstname} {self.parent_lastname}"
