import requests

from setting.endpoint import API_PROVINCE
from setting.general import api_key


def test():
    head = {
        "key": api_key
    }
    req = requests.post(API_PROVINCE, headers=head)
    print(req.json())
