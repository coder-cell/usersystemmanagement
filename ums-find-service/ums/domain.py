from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if self.value is None or len(self.value.strip()) < 8 or len(self.value.strip()) > 32:
            raise ValueError("Invalid Name")


@dataclass(frozen=True)
class PhoneNumber:
    value: int

    def __post_init__(self):
        if self.value < 9000000000:
            raise ValueError("Invalid Phone Number")


@dataclass
class User:
    _name = Name
    _phone = PhoneNumber
    _since = datetime.datetime

    @property
    def name(self) -> Name:
        return self._name

    @property
    def phone(self) -> PhoneNumber:
        return self._phone

    @property
    def since(self) -> datetime.datetime:
        return self._since

    @phone.setter
    def phone(self, phone: PhoneNumber) -> None:
        if phone is None:
            raise ValueError("Invalid Phone")
        self._phone = phone

    def __str__(self):
        return self.name.value + "[" + str(self.phone.value) + "] since " \
               + str(self.since)
