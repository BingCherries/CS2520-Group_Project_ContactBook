from dataclasses import dataclass

@dataclass
class Contact:
    '''Represents a single contact in a contact book'''
    id: int = None
    firstName: str = None
    middleName: str = None
    lastName: str = None
    phone: str = None
    email: str = None
    birthday: str = None
    memo: str = None

    def all(self):
        return (
            self.id,
            self.firstName,
            self.middleName,
            self.lastName,
            self.phone,
            self.email,
            self.birthday,
            self.memo,
        )



