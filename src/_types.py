import re
from typing import NewType, TypedDict, Union

Email = NewType('Email', str)


def check_email(email: str) -> Email:
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(email_regex, email):
        return Email(email)
    else:
        raise TypeError('Not email format')


class ShortUser(TypedDict):
    id: int
    name: str
    username: str
    email: Email
    address: dict[str, Union[str, dict[str, str]]]
    phone: str
    website: str
    company: dict[str, str]


class User(ShortUser):
    todos: list
    albums: str
    posts: str
