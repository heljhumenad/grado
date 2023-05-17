from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel


class CustomUserManager(UserManager):
    pass  # check if whats the use of UserManager


class CustomUser(AbstractUser):
    object = CustomUserManager()

    @property
    def get_user_account_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_user_email(self):
        return self.email


class Role(models.Model, TimeStampModel):
    class Meta:
        abstract = True

    ROLE_NAME = (
        ("Admin", "Administrator"),
        ("Parents", "Parents"),
        ("Teacher", "Teacher"),
        ("Editor", "Editor"),
        ("Approver", "Approver"),
    )

    role_name = models.CharField(
        max_length=200, choices=ROLE_NAME, blank=False, verbose_name=_("Role Name")
    )

    role_desc = models.CharField(
        max_length=200,
        verbose_name=_("Role Description"),
        blank=False,
    )

    role_mapping_id = models.CharField(
        max_length=200, verbose_name=_("Role Mapping"), blank=False
    )

    role_hash = models.CharField(
        max_length=200, verbose_name=_("Role Hash"), blank=False
    )
