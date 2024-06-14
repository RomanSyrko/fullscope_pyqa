import pytest


@pytest.mark.database
def test_database_connection(db_fixture):
    """
    Test the database connection.

    This test verifies that the database connection is successfully established by calling the 'test_connection' method
    of the 'db_fixture'.
    """
    db_fixture.test_connection()


@pytest.mark.database
def test_check_all_users(db_fixture):
    """
    Test retrieving all users from the database.

    This test retrieves all users from the database using the 'get_all_users' method of the 'db_fixture'.
    It then asserts that at least one user exists and checks the details of the first and second users.
    """
    users = db_fixture.get_all_users()  # Retrieve all users from the database

    assert len(users) > 0
    assert users[0][0] == 'Sergii'
    assert users[1][0] == 'Stepan'

    # Check that accessing the fourth user raises an IndexError
    # This is to ensure the list does not have a fourth user
    with pytest.raises(IndexError):
        assert users[3][0] == 'Ivan'


@pytest.mark.database
def test_check_user(db_fixture):
    """
    Test retrieving a specific user from the database.

    This test retrieves a user named 'Sergii' from the database using the 'get_user_address_by_name' method
    of the 'db_fixture'. It then asserts the user's address details.
    """
    user = db_fixture.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_update_product_quantity_by_id(db_fixture):
    """
    Test updating the quantity of a product by its ID.

    This test updates the quantity of a product with ID 1 to 25 using the 'update_product_quantity_by_id' method
    of the 'db_fixture'. It then selects the product's quantity again and asserts that it has been updated correctly.
    """
    db_fixture.update_product_quantity_by_id(1, 25)  # Set a new number of products for ID1
    water_qnt = db_fixture.select_product_quantity_by_id(1)  # Read the quantity of the product for ID1

    assert water_qnt[0][3] == 25


@pytest.mark.database
def test_select_product_quantity_by_id(db_fixture):
    """
    Test selecting product quantity by its ID.

    This test retrieves the quantity of a product with ID 1 using the 'select_product_quantity_by_id' method
    of the 'db_fixture'. It then asserts that the product name is 'soda', the quantity is 25,
    and 'Water' is not present in the product details.
    """
    soda = db_fixture.select_product_quantity_by_id(1)

    assert soda[0][1] == 'soda'
    assert soda[0][3] == 25
    assert 'Water' not in soda


@pytest.mark.database
def test_insert_product(db_fixture):
    """
    Test inserting a new product into the database.

    This test inserts a new product with ID 4, name 'cookies', description 'sweet', and quantity 50
    using the 'insert_product' method of the 'db_fixture'. It then selects the inserted product's details
    and asserts that the name, description, and quantity match the expected values.
    """
    db_fixture.insert_product(4, 'cookies', 'sweet', 50)
    water_qnt = db_fixture.select_product_quantity_by_id(4)

    assert water_qnt[0][1] == 'cookies'
    assert water_qnt[0][2] == 'sweet'
    assert water_qnt[0][3] == 50


@pytest.mark.database
def test_delete_product(db_fixture):
    """
    Test deleting a product from the database.

    This test first inserts a product with ID 99 into the database using the 'insert_product' method
    of the 'db_fixture', then deletes it using the 'delete_product_by_id' method. After deletion,
    it checks if the product with ID 99 no longer exists in the database by selecting its quantity,
    and asserts that the length of the returned data is 0.
    """
    db_fixture.insert_product(99, 'Test', 'Data', 999)  # Create data in the database
    db_fixture.delete_product_by_id(99)  # Delete the data we just created
    qnt = db_fixture.select_product_quantity_by_id(99)  # Check whether our data is in the table

    assert len(qnt) == 0


@pytest.mark.database
def test_get_detailed_orders(db_fixture):
    """
    Test getting detailed orders from the database.

    This test retrieves detailed order information from the database using the 'get_detailed_orders'
    method of the 'db_fixture'. It asserts that only one order is returned, and checks the details
    of this order against the expected values.
    """
    order = db_fixture.get_detailed_orders()

    assert len(order) == 2
    assert order[0][0] == 1
    assert order[0][1] == 'Sergii'
    assert order[0][2] == 'soda'
    assert order[0][3] == 'sweet'


@pytest.mark.database
def test_check_all_orders(db_fixture):
    """
    Test checking all orders in the database.

    This test retrieves all orders from the database using the 'check_all_orders' method of the 'db_fixture'.
    It asserts that the type of the order date is a string and that the total number of orders is 2.
    """
    result = db_fixture.check_all_orders()

    assert type(result[0][3]) == str
    assert len(result) == 2


@pytest.mark.database
def test_insert_order(db_fixture):
    """
    Test inserting an order into the database.

    This test inserts a new order with ID 2, customer ID 3, product ID 4, and order date '31:05:24'
    into the database using the 'insert_order' method of the 'db_fixture'. It then checks if the
    order was inserted correctly by verifying its details in the database.
    """
    db_fixture.insert_order(2, 3, 4, '31:05:24')
    result = db_fixture.check_all_orders()

    assert result[1][3] == '31:05:24'
    assert result[0][1] != 0
