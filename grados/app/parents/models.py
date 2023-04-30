from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.accounts.models import CustomUser


class Parents(models.Model, TimeStampModel):
    
    class Meta:
        db_table = _('parents')
        verbose_name = _('Parent')
        verbose_name_plural = _('Parents')
        ordering = ['id']

    def __str__(self):
        return f"{self.parent_firstname} {self.parent_lastname}"
