import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def create_db():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_store)



async def sql_insert_store(name_product, size, price, photo, product_id, category, info_product):
    cursor.execute(queries.INSERT_store_query, (
        name_product, size, price, photo, product_id, category, info_product
    ))
    db.commit()


async def sql_insert_order(product_id, size, quantity, contact):
    cursor.execute(queries.INSERT_order_query,
    (product_id, size, quantity, contact))
    db.commit()


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store
    """).fetchall()
    conn.close()
    return products








