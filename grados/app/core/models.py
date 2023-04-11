from django.db import models
from django.utils.translation import gettext as _

class TimeStampModel(models.DateTimeField):
    class Meta:
        abstract = True
    
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = _('Created At')
    )

    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = _('Updated At')
    )