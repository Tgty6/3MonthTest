CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, product_id, category, info_product)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""


CREATE_TABLE_orders = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    size TEXT,
    quantity TEXT,
    contact TEXT
)
"""

INSERT_order_query = """
    INSERT INTO order (product_id, size, quantity, contact)
    VALUES (?, ?, ?, ?)
"""