from datetime import datetime as dt


class Person:
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 date_of_birth: dt = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth.isoformat()
        self.full_name = self._full_name()

    def _full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        if self.date_of_birth != None:
            # return f'{self.first_name} {self.last_name} ({self.date_of_birth.strftime('%Y')}.)'
            return f'{self.full_name} ({self.date_of_birth.strftime('%Y')}.)'
        else:
            return f'{self.full_name}'
