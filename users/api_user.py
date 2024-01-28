import json
import requests
from data import ConstantData, EndPointData


class ApiClient:

    def __init__(self):
        self.base_url = EndPointData.BASE_URL
        self.headers = ConstantData.DEFAULT_HEADERS

    def post(self, path, payload):
        response = requests.post(url=self.base_url + path,
                                 headers=self.headers,
                                 data=json.dumps(payload))
        return response

    def get(self, path, authorization=None):
        if authorization is not None:
            response = requests.get(url=self.base_url + path,
                                    headers={"accept": "application/json",
                                             "Content-Type": "application/json",
                                             'Authorization': authorization
                                             })
        else:
            response = requests.get(url=self.base_url + path,
                                    headers=self.headers)
        return response

    def patch(self, path, payload, authorization=None):
        response = requests.patch(url=self.base_url + path,
                                  headers={'Authorization': authorization},
                                  data=json.dumps(payload))
        return response

    def delete(self, path, authorization=None):
        response = requests.delete(url=self.base_url + path,
                                   headers={'Authorization': authorization})
