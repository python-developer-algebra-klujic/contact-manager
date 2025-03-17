from typing import List
from datetime import datetime as dt

from features.customers.models.customers import Customer
from features.shared.models.persons import Person


class Employee(Person):
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 customers: List[Customer] = [],
                 date_of_birth: dt = None):
        super().__init__(id, first_name, last_name, date_of_birth)
        self.customers = customers

    def __repr__(self):
        return f'{self.full_name} ({len(self.customers)})'
