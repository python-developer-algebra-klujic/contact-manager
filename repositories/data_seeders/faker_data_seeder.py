from faker import Faker
from datetime import datetime as dt

from features import Contact


class FakerDataSeeder:
    def __init__(self,
                 localization: str = ''):
        self.localization = localization
        self.faker_obj = None

        self._initialize_faker()


    def _initialize_faker(self):
        if self.localization:
            self.faker_obj = Faker(self.localization)
        else:
            self.faker_obj = Faker()

    def seed_contacts(self):
        first_name, last_name = self.faker_obj.name().split(' ')
        email = self.faker_obj.email()
        phone = self.faker_obj.phone_number()
        website = self.faker_obj.url()
        date_of_birth = self.faker_obj.date()
        date_of_birth = dt.strptime(date_of_birth, '%Y-%m-%d')

        return Contact(1,
                       first_name,
                       last_name,
                       email,
                       phone,
                       website,
                       date_of_birth)

