from typing import List

from features.contacts.models.contacts import Contact
from features.shared.models.companies import Company


class Customer(Company):
    def __init__(self,
                 id: int,
                 name: str,
                 vat_id: str,
                 headquarter: str,
                 contacts: List[Contact] = []):
        super().__init__(id, name, vat_id, headquarter)
        self.contacts = contacts

    def __repr__(self):
        return f'{self.name} ({self.vat_id}) / ({len(self.contacts)})'
