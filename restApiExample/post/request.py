import requests
from requests.auth import HTTPBasicAuth


class Api:

    def get_users(self):
        r = requests.get(f'http://127.0.0.1:8000/api-auth/posts/1/?format=json')
        return r.json()

    def get_posts(self):
        r = requests.get(f'http://127.0.0.1:8000/api-auth/posts/')
        return r.json

