# Teacher Factory
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Factory

from grados.app.teachers.models import Teacher


faker = Factory.create()

# TODO: Add some faker data for this class
class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    birth_date = faker.date(
        pattern = '%m/%d/%Y',
        end_datetime = None,
    )

    designation_as = faker.random_elements(
        elements = (
            'Mrs.',
            'Mr.',
            'Miss',
            'Dr.',
            'Atty.'
        )
    )
