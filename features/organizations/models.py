from features.shared.models.companies import Company
from features.shared.models.persons import Person


class Organization(Company):
    pass


class Employee(Person):
    pass


class Customer(Company):
    pass


class Contact(Person):
    pass
