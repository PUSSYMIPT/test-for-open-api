from .utils.product_processing import find_product, create_product, simply_create_product, get_tester
import pytest



@pytest.mark.parametrize('create_product', [('new_229_product',)], indirect=True)
def test_place_new_product_name(create_product):
    print(create_product)
    assert create_product['name'] == 'new_229_product'


@pytest.mark.parametrize('find_product', [('new_229_product', )], indirect=True)
def test_find_placed_product(find_product):
    assert find_product['total'] != 0


@pytest.mark.parametrize('find_product', [('new_225_product', 'new_226_product', 'new_227_product')], indirect=True)
def test_find_not_placed_product(find_product):
    assert find_product['total'] == 0


def test_id_sequence():
    first_id = simply_create_product()['id']
    second_id = simply_create_product()['id']
    assert first_id == second_id - 1


def test_add_and_remove():
    tester = get_tester()
    current_id = tester.create_item('new__product')['id']
    assert tester.find_item_by_id(current_id)['total'] != 0
    tester.delete_item_by_id(current_id)
    assert tester.find_item_by_id(current_id)['total'] == 0


def test_remove_all_created():
    tester = get_tester()
    tester.delete_all_items()
    response = tester.find_item_like('new_*')
    assert response['total'] == 0


