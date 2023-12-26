import requests
from assertpy import assert_that
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    req = requests.post("https://api.rajaongkir.com/starter/provinces", headers=head)

    # verification
    status_code = req.status_code
    latency = req.elapsed.microseconds

    # assert
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)
