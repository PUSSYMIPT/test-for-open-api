from .utils.service_processing import find_service, create_service, simply_create_service, get_tester
import pytest


@pytest.mark.parametrize('create_service', [('new_229_service',)], indirect=True)
def test_place_new_service_name(create_service):
    print(create_service)
    assert create_service['name'] == 'new_229_service'


@pytest.mark.parametrize('find_service', [('new_229_service',)], indirect=True)
def test_find_placed_service(find_service):
    assert find_service['total'] != 0


@pytest.mark.parametrize('find_service', [('new_225_service', 'new_226_service', 'new_227_service')], indirect=True)
def test_find_not_placed_service(find_service):
    assert find_service['total'] == 0


def test_id_sequence():
    first_id = simply_create_service()['id']
    second_id = simply_create_service()['id']
    assert first_id == second_id - 1


def test_add_and_remove():
    tester = get_tester()
    current_id = tester.create_item('new__service')['id']
    assert tester.find_item_by_id(current_id)['total'] != 0
    tester.delete_item_by_id(current_id)
    assert tester.find_item_by_id(current_id)['total'] == 0


def test_remove_all_created():
    tester = get_tester()
    tester.delete_all_items()
    response = tester.find_item_like('new_*')
    assert response['total'] == 0
