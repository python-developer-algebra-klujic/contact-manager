from datetime import datetime as dt

from features.shared.models.persons import Person


class Contact(Person):
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 email: str,
                 phone: str,
                 website: str = '',
                 date_of_birth: dt = None):
        super().__init__(id, first_name, last_name, date_of_birth)
        self.email = email
        self.phone = phone
        self.website = website

    def __repr__(self):
        return f'{self.full_name} (email: {self.email}; tel: {self.phone})'
