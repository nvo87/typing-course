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
from returns._internal.pipeline.flow import flow
from returns.pointfree import bind
from returns.result import Result, safe

from _types import Email, Post, ShortUser, check_email


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


def fetch_user_posts(user_id: int) -> Result[list['Post'], Exception]:
    return flow(
        user_id,
        _make_request,
        bind(_parse_json),
    )


@safe
def _make_request(user_id: int) -> requests.Response:
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/posts'
    response = requests.get(url)
    response.raise_for_status()
    return response


@safe
def _parse_json(response: requests.Response) -> list['Post']:
    return response.json()


if __name__ == '__main__':
    emails = read_emails('../data/1.txt')
    users = fetch_users()

    users = [user for user in users if user['email'] in emails]

    post = fetch_user_posts(1)

    # TODO
    # implement smth like
    # post.good_result(attach_to_user)
    # post.bad_result(sentry_sdk.capture_exception(error))

