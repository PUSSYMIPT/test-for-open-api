from .utils.store_processing import find_store, create_store, simply_create_store, get_tester
import pytest


@pytest.mark.parametrize('create_store', [('new_229_store',)], indirect=True)
def test_place_new_store_name(create_store):
    print(create_store)
    assert create_store['name'] == 'new_229_store'


@pytest.mark.parametrize('find_store', [('new_229_store',)], indirect=True)
def test_find_placed_store(find_store):
    assert find_store['total'] != 0


@pytest.mark.parametrize('find_store', [('new_225_store', 'new_226_store', 'new_227_store')], indirect=True)
def test_find_not_placed_store(find_store):
    assert find_store['total'] == 0


def test_id_sequence():
    first_id = simply_create_store()['id']
    second_id = simply_create_store()['id']
    assert first_id == second_id - 1


def test_add_and_remove():
    tester = get_tester()
    current_id = tester.create_item('new__store')['id']
    assert tester.find_item_by_id(current_id)['total'] != 0
    tester.delete_item_by_id(current_id)
    assert tester.find_item_by_id(current_id)['total'] == 0


def test_remove_all_created():
    tester = get_tester()
    tester.delete_all_items()
    response = tester.find_item_like('new_*')
    assert response['total'] == 0
