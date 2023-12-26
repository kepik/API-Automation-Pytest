import requests
from assertpy import assert_that
from jsonschema import validate as validate_json_schema

from jsonschemas.schema_cost import *
from setting.endpoint import API_COST
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    payload = {
        "origin":"1",
        "destination":"60",
        "weight":1000,
        "courier":"pos"
    }
    req = requests.post(API_COST, headers=head, json=payload)
#    print(req.json())

    # verification
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    results = req.json().get("rajaongkir")["results"]

    # assert
    assert_that(status_code).is_equal_to(200)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("OK")
    validate_json_schema(instance=req.json(), schema=schema_list_cost_normal)
