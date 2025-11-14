import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('ecommerce.db')

# Read the SQL query from file
with open('join_query.sql', 'r') as f:
    query = f.read()

# Execute the query and load results into a DataFrame
df = pd.read_sql_query(query, conn)

# Print results in a nice table format
print("\n" + "="*100)
print("JOIN QUERY RESULTS")
print("="*100)
print(f"\nTotal rows: {len(df)}\n")
print(df.to_string(index=False))
print("\n" + "="*100)

# Close the connection
conn.close()

