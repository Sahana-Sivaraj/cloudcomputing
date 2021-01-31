# application1/frontend/api/UserClient.py
import requests
from flask import session, request


class UserClient:
    @staticmethod
    def post_login(json):
        api_key = False
        payload = {
            'username': json.username.data,
            'password': json.password.data
        }
        url = 'http://cuser-service:5001/api/user/login'
        response = requests.request("POST", url=url, data=payload)
        return response.json()

    @staticmethod
    def get_user():
        headers = {
            'Authorization': 'Basic ' + session['username']
        }
        url = 'http://cuser-service:5001/api/user'
        response = requests.request(method="GET", url=url, headers=headers)
        user = response.json()
        return user

    @staticmethod
    def post_user_create(json):
        user = False
        payload = {
            'email': json.email.data,
            'password': json.password.data,
            'first_name': json.first_name.data,
            'last_name': json.last_name.data,
            'username': json.username.data
        }
        url = 'http://cuser-service:5001/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def does_exist(username):
        url = 'http://cuser-service:5001/api/user/' + username + '/exists'
        response = requests.request("GET", url=url)
        return response.status_code == 200

