from typing import List

from features.customers.models.customers import Customer
from features.employees.models.employees import Employee
from features.shared.models.companies import Company


class Organization(Company):
    def __init__(self,
                 id: int,
                 name: str,
                 vat_id: str,
                 headquarter: str,
                 employees: List[Employee] = [],
                 customers: List[Customer] = []):
        super().__init__(id, name, vat_id, headquarter)
        self.employees = employees
        self.customers = customers

    def __repr__(self):
        return super().__repr__()
