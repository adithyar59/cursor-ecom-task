import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('ecommerce.db')

print("\n" + "="*80)
print("ECOMMERCE DATABASE - ALL TABLES")
print("="*80)

# List of tables
tables = ['customers', 'products', 'orders', 'order_items', 'payments']

for table in tables:
    print(f"\n{'='*80}")
    print(f"TABLE: {table.upper()}")
    print('='*80)
    
    # Read table into DataFrame
    df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
    
    print(f"\nTotal rows: {len(df)}\n")
    print(df.to_string(index=False))
    print()

# Close connection
conn.close()

print("\n" + "="*80)
print("END OF DATABASE VIEW")
print("="*80)

