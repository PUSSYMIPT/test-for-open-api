import pytest
import requests
from .utils.simple_request_block import request_status
from .utils.html_parsing import load_soup
import json

with open('../configs.json', 'r') as inp:
    HOST = json.load(inp)['host']


@pytest.mark.parametrize('request_status', [(HOST,)], indirect=True)
def test_response(request_status):
    assert request_status == 200


@pytest.mark.parametrize('load_soup', [(HOST,)], indirect=True)
def test_start_page_content(load_soup):
    assert len(load_soup.findAll('h3')) == 6


def test_remove_all_services():
    requests.delete(HOST+'/services')


def test_remove_all_products():
    requests.delete(HOST+'/products')


def test_remove_all_stores():
    requests.delete(HOST+'/stores')


def test_service_is_up():
    response = requests.get(HOST+'/healthcheck')
    assert response.status_code == 200


