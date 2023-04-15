from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext as _


class CustomUserManager(UserManager):
    pass # check if whats the use of UserManager

class CustomUser(AbstractUser):
    object = CustomUserManager()

    @property
    def get_user_account_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    @property
    def get_user_email(self):
        return self.email