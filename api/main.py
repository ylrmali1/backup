import requests

class Api:
    def __init__(self, api_url):
        self.api_url = api_url

    def get(self):
        r = requests.get(f'')
