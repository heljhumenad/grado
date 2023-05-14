from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import (
    BasicInfo,
    AddressInfo
)
from grados.app.core.models import TimeStampModel
from grados.app.students.models import Student


class Parent(TimeStampModel, BasicInfo, AddressInfo, ):

    student_id = models.ForeignKey(
        Student,
        on_delete = models.CASCADE,
        verbose_name = _('Students')
    )

    occupation = models.CharField(
        max_length = 200,
        verbose_name = _('Occupation'),
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

    email_address = models.EmailField(
        max_length = 200,
        verbose_name = _('Email Address'),
        blank = False
    )
    # TODO: Check if this field is need to be Boolean Field 
    # TODO: What will be the design if the user will pick No as Legal Guardian
    legal_guardian = models.BooleanField(
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
