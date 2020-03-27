import pytest
from _pytest.fixtures import SubRequest
import requests


@pytest.fixture
def request_answer(request: SubRequest):
    param = getattr(request, 'param', None)
    ans = requests.get(str(param[0]))
    yield ans


@pytest.fixture
def request_status(request: SubRequest):
    param = getattr(request, 'param', None)
    ans = requests.get(str(param[0]))
    yield ans.status_code


@pytest.fixture
def request_content(request: SubRequest):
    param = getattr(request, 'param', None)
    ans = requests.get(str(param[0]))
    yield ans.content


@pytest.fixture
def request_json(request: SubRequest):
    param = getattr(request, 'param', None)
    ans = requests.get(str(param[0]))
    yield ans.json()
