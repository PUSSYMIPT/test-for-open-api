from .utils.product_processing import get_tester as get_product_tester
from .utils.store_processing import get_tester as get_store_tester
from .utils.service_processing import get_tester as get_service_tester


def test_all_add_and_remove():
    product_tester = get_product_tester()
    store_tester = get_store_tester()
    service_tester = get_service_tester()

    for i in range(100):
        product_tester.create_item('new__product')
        store_tester.create_item('new__store')
        service_tester.create_item('new__service')

    product_tester.delete_all_items()
    store_tester.delete_all_items()
    service_tester.delete_all_items()
    assert product_tester.find_item_like('new_*')['total'] == 0
    assert store_tester.find_item_like('new_*')['total'] == 0
    assert service_tester.find_item_like('new_*')['total'] == 0
