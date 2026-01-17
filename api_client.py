import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint, headers=self.headers)

    def put(self, endpoint, payload):
        return requests.put(self.base_url + endpoint, json=payload, headers=self.headers)
