import pytest
from _pytest.fixtures import SubRequest
import json
from .items_tester import ItemsTester


with open('../configs.json', 'r') as inp:
    HOST = json.load(inp)['host']

DEFAULT_PAYLOAD = {
        'name': 'name',
        'type': 'HardGood',
        'upc': '12345676',
        'price': 9.99,
        'description': 'This is a placeholder request for creating a new product.',
        'model': 'NP1234'
    }

TESTER = ItemsTester(host=HOST, label='products', default_payload=DEFAULT_PAYLOAD)


@pytest.fixture
def create_product(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.create_item(name=param[0])
    return response


@pytest.fixture
def find_product(request: SubRequest):
    param = getattr(request, 'param', None)
    response = TESTER.find_item(name=param[0])
    return response


def simply_create_product(product_name: str = None):
    if product_name is None:
        product_name = "New Product"
    response = TESTER.create_item(product_name)
    return response


def get_tester():
    return TESTER