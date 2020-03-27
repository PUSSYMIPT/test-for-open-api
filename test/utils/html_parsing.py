import requests
from bs4 import BeautifulSoup
import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture
def load_soup(request: SubRequest):
    param = getattr(request, 'param', None)
    ans = requests.get(str(param[0]))
    soup = BeautifulSoup(ans.content)
    yield soup
