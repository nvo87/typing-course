"""
1. read csv
2. get users.json https://jsonplaceholder.typicode.com/users/
3. read users.json
4. find id by email
5. get post, albums,todos
6. add post, albums,todos to user.json
7. save users/${userId}/user.json to disk
8. logging!
"""

import requests

from _types import Email, ShortUser, check_email


def read_emails(file) -> list[Email]:
    emails = []
    with open(file, 'r') as emails_file:
        for email in emails_file:
            try:
                email = email.strip()
                email = check_email(email)
                emails.append(email)
            except TypeError:
                continue
        return emails


def fetch_users() -> list[ShortUser]:
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    emails = read_emails('../data/1.txt')
    users = fetch_users()

    users = [user for user in users if user['email'] in emails]
