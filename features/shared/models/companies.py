


class Company:
    def __init__(self,
                 id: int,
                 name: str,
                 vat_id: str,
                 headquarter: str):
        self.id = id
        self.name = name
        self.vat_id = vat_id
        self.headquarter = headquarter

    def __repr__(self):
        return f'{self.name} ({self.vat_id})'
