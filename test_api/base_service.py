import pytest
import requests
from logger import logger


class BaseService:

    @staticmethod
    def request(method, url, token, body, code):
        if pytest.token:
            headers = {"Authorization": f"Bearer {pytest.token}"}
        else:
            headers = None
        try:
            response = requests.request(method, url, headers=headers, json=body)
            if code is None:
                response.raise_for_status()
            else:
                assert response.status_code == code
            logger.info("OK. URL: %s, CODE: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None

    def get(self, url, token, code=None):
        return self.request("GET", url, token, None, code)

    def post(self, url, token, body=None, code=None):
        return self.request("POST", url, token, body, code)

    def put(self, url, token, body=None, code=None):
        return self.request("PUT", url, token, body, code)

    def delete(self, url, token, body=None, code=None):
        return self.request("DELETE", url, token, body, code)
