from dataclasses import dataclass

"""Data generation details for contact us and autocomplete pages."""


@dataclass
class NewUser:
    first_name: str = None
    last_name: str = None
    email: str = None
    comments: str = None


@dataclass
class Food:
    food_name: list = None
