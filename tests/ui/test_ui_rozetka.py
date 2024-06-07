import pytest
import time

from modules.ui.page_objects.rozetka_search import SearchProduct, CheckBasket


@pytest.mark.ui_rozetka
def test_ui_rozetka_search():
    """
    Test to search for a product on the Rozetka website and verify the page title.
    """
    search_product = SearchProduct()

    # Open the Rozetka search page
    search_product.go_to()

    # Search for the specified product
    search_product.try_to_find('Iphone 15 pro max 512')

    # Check that the page title matches the expected search results title
    assert search_product.check_title('ROZETKA — Результати пошуку: "Iphone 15 pro max 512" | Пошук')

    # Close the browser
    search_product.close()


@pytest.mark.ui_rozetka_basket
def test_ui_rozetka_basket():
    """
    Test to add a product to the basket on the Rozetka website, verify the basket contains the product,
    and then remove the product, verifying the basket is empty.
    """
    check_basket = CheckBasket()

    # Open the Rozetka product page
    check_basket.go_to()

    # Add the product to the basket
    check_basket.add_product()
    time.sleep(1)  # Wait for the basket to update

    # Verify the basket contains the product
    res = check_basket.check_basket_contain()
    assert res.text == '1'  # Check that the basket shows 1 item
    assert res.text != ''  # Check that the basket is not empty
    assert res.text is not None  # Check that the basket text is not None

    # Remove the product from the basket
    check_basket.delete_product()
    time.sleep(1)  # Wait for the basket to update

    # Verify the basket is empty
    res = check_basket.check_basket_not_contain('Кошик порожній')
    assert res is False  # Check that the basket does not contain the text 'Кошик порожній'

    # Close the browser
    check_basket.close()
