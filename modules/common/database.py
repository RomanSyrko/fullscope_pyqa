import sqlite3


class Database:
    """ A class to interact with a SQLite database. """

    def __init__(self):
        """ Initializes the Database class and establishes a connection to the SQLite database. """
        self.connection = sqlite3.connect('/Users/romansyrko/PycharmProjects/fullscope_pyqa' + '/qa_auto_tests.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        """ Tests the connection to the SQLite database by executing a query to get the SQLite version. """
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"SQLite Database Version is: {record}")

    def get_all_users(self):
        """ Retrieves all users from the 'customers' table in the database. """
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        """ Retrieves the address details of a user by their name from the 'customers' table. """
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name='{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_quantity_by_id(self, product_id, qnt):
        """ Updates the quantity of a product with the specified ID. """
        query = f"UPDATE products SET quantity = {qnt} WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_quantity_by_id(self, product_id):
        """ Retrieves the details of a product by its ID from the 'products' table. """
        query = f"SELECT * FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        """ Inserts a new product into the 'products' table or replaces an existing one if the ID matches. """
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
        VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        """ Deletes a product with the specified ID from the 'products' table. """
        query = f"DELETE FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        """ Retrieves detailed order information including customer name, product name, description, and order date. """
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
        FROM orders \
        JOIN customers ON orders.customer_id = customers.id \
        JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def check_all_orders(self):
        """ Retrieves all orders from the 'orders' table. """
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_order(self, id, customer_id, product_id, order_date):
        """ Inserts a new order into the 'orders' table or replaces an existing one if the ID matches. """
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
        VALUES ({id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()
