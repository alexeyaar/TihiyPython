import pytest
import logging


class Requester:
    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.headers = self.base_headers.copy()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)


    def sends_req(self, method, endpoint,data =None,headers = None , expected_status=200,need_logging = True):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method,url, json=data)
        return response
