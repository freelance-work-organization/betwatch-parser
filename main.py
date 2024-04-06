import json

import requests
from bs4 import BeautifulSoup


class BetWatchParser:
    def __init__(self):
        self.session = requests.Session()
        with open('cookies.json', 'r') as cookie:
            self.session.cookies = json.loads(cookie.read())

    def __del__(self):
        with open('cookies.json', 'w') as cookie:
            cookie.write(json.dumps(self.session.cookies))

