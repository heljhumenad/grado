from django.db import models
from django.utils.translation import gettext as _

from grados.app.core.models import TimeStampModel
from grados.app.teachers.models import Teacher

# TODO: Create normalize table for students and teacher
class Student(model.Model, TimeStampModel):
    pass

