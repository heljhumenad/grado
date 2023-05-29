from django.db import models
from django.utils.translation import gettext as _


class GradoTimeStampModel(models.DateTimeField):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))


class GradoBasicInfo(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=200, verbose_name=_("First Name"), blank=False
    )

    last_name = models.CharField(
        max_length=200, verbose_name=_("Last Name"), blank=False
    )

    middle_name = models.CharField(
        max_length=200, verbose_name=_("Middle Name"), blank=False
    )


class GradoAddressInfo(models.Model):
    class Meta:
        abstract = True

    address1 = models.CharField(
        max_length=200, verbose_name=_("Address 1"), blank=False
    )

    address2 = models.CharField(
        max_length=200, verbose_name=_("Address 2"), blank=False
    )
