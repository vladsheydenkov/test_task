"""
This module provides CRUD operation tests for users endpoint
"""


from copy import copy
from rest_framework import status
import requests
import json
import unittest


ENDPOINT = "https://petstore.swagger.io/v2/user"
VALID_USER = {
    "id": 0,
    "username": "test_user",
    "firstName": "test_name",
    "lastName": "test_last_name",
    "email": "test_email",
    "password": "test_password",
    "phone": "+000",
    "userStatus": 0
}


class UserCreationTest(unittest.TestCase):
    """
    Test for creating new a new user
    """

    def setUp(self) -> None:
        self.url = ENDPOINT
        self.valid_user = VALID_USER
        self.valid_data = json.dumps(self.valid_user)
        self.invalid_data = 'invalid data'
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def test_create_valid_user(self):
        """
        Create new user using valid data
        """
        response = requests.post(self.url, data=self.valid_data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        global VALID_USER

    def test_create_invalid_user(self):
        """
        Create new user using invalid data
        """
        response = requests.post(self.url, data=self.invalid_data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetUserTest(unittest.TestCase):
    """
    Test for GET user
    """

    def setUp(self) -> None:
        self.username = VALID_USER.get('username')
        self.url = ENDPOINT + '/' + self.username
        self.invalid_url = ENDPOINT + '/' + 'fg123lkjppppp1231[]fd:{}'

    def test_get_valid_user(self):
        """
        Get user by username
        """
        response = requests.get(self.url)
        fetched_user = response.json()
        fetched_user_id = response.json().get('id')
        valid_user = copy(VALID_USER)
        valid_user['id'] = fetched_user_id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(valid_user, fetched_user)

    def test_get_invalid_user(self):
        """
        Seems that user1(it supposed to be used for testing purpose) doesn't work correctly
        """
        response = requests.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class LoginUserTest(unittest.TestCase):
    """
    Test for login
    """

    def setUp(self) -> None:
        self.url = ENDPOINT + '/' + 'login'
        self.username = VALID_USER.get('username')
        self.password = VALID_USER.get('password')

    def test_user_login(self):
        """
        Login using credentials
        """
        response = requests.get(self.url, params={'username': self.username,
                                                  'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(unittest.TestCase):
    """
    Test for user update
    """
    def setUp(self) -> None:
        self.url = ENDPOINT + '/' + VALID_USER.get('username')
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.updated_user = json.dumps({
            "id": 0,
            "username": "new_test_name",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        })

    def test_user_update(self):
        """
        User update
        """
        response = requests.put(self.url, data=self.updated_user, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(unittest.TestCase):
    """
    Test possibility to delete user
    """
    def setUp(self) -> None:
        self.url = ENDPOINT
        self.new_user = {
            "id": 0,
            "username": 'lskokoskdkflsdkjflskdjf',
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
        self.user_url = self.url + '/' + self.new_user.get('username')
        self.new_user_json = json.dumps(self.new_user)

    def test_user_creation(self):
        """
        Creates new user to delete it
        """
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}
        response = requests.post(self.url, data=self.new_user_json, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        """
        Login new user
        """
        url = self.url + '/' + 'login'
        response = requests.get(url, params={'username': self.new_user.get('username'),
                                             'password': self.new_user.get('password')})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """
        Delete created user
        """
        response = requests.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def check_if_deleted(self):
        """
        Check if user was deleted
        """
        response = requests.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
