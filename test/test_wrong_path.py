import pytest
import requests
from .utils.simple_request_block import request_status, request_json


@pytest.mark.parametrize('request_status', [('http://localhost:3030/path/to/nowhere',)], indirect=True)
def test_incorrect_path_status(request_status):
    assert request_status == 404


@pytest.mark.parametrize('request_json', [('http://localhost:3030/path/to/nowhere',)], indirect=True)
def test_incorrect_path_json(request_json):
    assert request_json['name'] == 'NotFound'
    assert request_json['message'] == 'Page not found'
