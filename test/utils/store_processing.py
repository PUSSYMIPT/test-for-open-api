import json
import pytest
from _pytest.fixtures import SubRequest

from test.utils.items_tester import ItemsTester

with open('../configs.json', 'r') as inp:
    HOST = json.load(inp)['host']

DEFAULT_PAYLOAD = {
    'name': 'new__store',
    'type': 'BigBox',
    'address': 'fake_str',
    'state': 'MN',
    'zip': "55123",
    "lat": 44.969658,
    "lng": -93.449539,
    "city": "Moscow"
}

TESTER = ItemsTester(host=HOST, label='stores', default_payload=DEFAULT_PAYLOAD)


@pytest.fixture
def create_store(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.create_item(name=param[0])
    return response


@pytest.fixture
def find_store(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.find_item(name=param[0])
    return response


def simply_create_store(product_name: str = None):
    if product_name is None:
        product_name = "new__store"
    response = TESTER.create_item(product_name)
    return response


def simply_delete_store(store_id):
    TESTER.delete_item_by_id(store_id)


def create_custom_store(payload):
    TESTER.create_item(name=payload['name'], payload=payload)


def get_tester():
    return TESTER
