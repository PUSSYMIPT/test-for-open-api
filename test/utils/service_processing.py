import json
import pytest
import requests
from _pytest.fixtures import SubRequest

from test.utils.items_tester import ItemsTester

with open('../configs.json', 'r') as inp:
    HOST = json.load(inp)['host']

DEFAULT_PAYLOAD = {
    'name': 'name',
}

TESTER = ItemsTester(host=HOST, label='services', default_payload=DEFAULT_PAYLOAD)


@pytest.fixture
def create_service(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.create_item(name=param[0])

    return response


@pytest.fixture
def find_service(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.find_item(name=param[0])
    return response


def simply_create_service(product_name: str = None):
    if product_name is None:
        product_name = "new_230_service"
    response = TESTER.create_item(product_name)

    return response


def get_tester():
    return TESTER
