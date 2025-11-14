import pandas as pd
import sqlite3
import os

# Create SQLite database connection
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables
print("Creating tables...")

# Customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    city TEXT
)
''')

# Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

# Order items table
cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

# Payments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL,
    payment_date TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
)
''')

print("Tables created successfully!")

# Read CSV files and insert data
print("Reading CSV files and inserting data...")

# Read and insert customers
if os.path.exists('data/customers.csv'):
    df_customers = pd.read_csv('data/customers.csv')
    df_customers.to_sql('customers', conn, if_exists='replace', index=False)
    print(f"Inserted {len(df_customers)} customers")

# Read and insert products
if os.path.exists('data/products.csv'):
    df_products = pd.read_csv('data/products.csv')
    df_products.to_sql('products', conn, if_exists='replace', index=False)
    print(f"Inserted {len(df_products)} products")

# Read and insert orders
if os.path.exists('data/orders.csv'):
    df_orders = pd.read_csv('data/orders.csv')
    df_orders.to_sql('orders', conn, if_exists='replace', index=False)
    print(f"Inserted {len(df_orders)} orders")

# Read and insert order items
if os.path.exists('data/order_items.csv'):
    df_order_items = pd.read_csv('data/order_items.csv')
    df_order_items.to_sql('order_items', conn, if_exists='replace', index=False)
    print(f"Inserted {len(df_order_items)} order items")

# Read and insert payments
if os.path.exists('data/payments.csv'):
    df_payments = pd.read_csv('data/payments.csv')
    df_payments.to_sql('payments', conn, if_exists='replace', index=False)
    print(f"Inserted {len(df_payments)} payments")

# Commit changes and close connection
conn.commit()
conn.close()

print("Ingestion successful")

