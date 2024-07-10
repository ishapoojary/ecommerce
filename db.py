import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='ecommerce_user',
        password='EUNWOO@123#',
        database='ecommerce'
    )

def get_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    connection.close()
    return products

def get_product(product_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
    product = cursor.fetchone()
    connection.close()
    return product

def add_to_cart(product_id, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO cart (product_id, quantity) VALUES (%s, %s)', (product_id, quantity))
    connection.commit()
    connection.close()

def remove_from_cart(product_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM cart WHERE product_id = %s', (product_id,))
    connection.commit()
    connection.close()

def get_cart_items():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT products.id, products.name, products.price, products.image_url, cart.quantity
        FROM cart
        JOIN products ON cart.product_id = products.id
    ''')
    cart_items = cursor.fetchall()
    connection.close()
    print(f"Cart items: {cart_items}") 
    return cart_items

def get_search_results(query):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products WHERE name LIKE %s', (f'%{query}%',))
    products = cursor.fetchall()
    connection.close()
    return products