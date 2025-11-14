## Overview

Small demo project that builds an `ecommerce.db` SQLite database from CSV seed files and showcases a multi-table join (`join_query.sql`) that surfaces customer orders with product and revenue information.

## Data Description

- `customers`: id, name, contact info, and city for each shopper.
- `products`: catalog of sellable items with category and unit price.
- `orders`: individual purchases keyed to customers with order date and status.
- `order_items`: line items that connect orders to specific products and purchased quantities.
- `payments`: settlement records for each order (amount, method, date).

All CSV sources live under `data/` and are ingested into SQLite via `ingest_data.py`.

## File Structure

- `data/` – raw CSVs for every table listed above.
- `ecommerce.db` – SQLite database produced after ingestion.
- `ingest_data.py` – creates tables and loads CSV contents into SQLite.
- `view_tables.py` – prints every table in `ecommerce.db` for a quick sanity check.
- `join_query.sql` – SELECT statement joining customers, orders, order_items, and products.
- `run_query.py` – executes `join_query.sql` and prints the result as a formatted table.

## How to View Tables and Query Results

1. **Install requirements**  
   Ensure Python 3.9+ is available, then install dependencies:  
   `pip install pandas`

2. **Build or refresh the database**  
   `python ingest_data.py`  
   This recreates the tables (if needed) and loads the CSV data into `ecommerce.db`.

3. **Inspect raw tables**  
   `python view_tables.py`  
   Each table prints to the console with row counts and full contents.

4. **Run the sample join**  
   `python run_query.py`  
   Reads `join_query.sql`, executes it against `ecommerce.db`, and displays combined customer/order/product details plus calculated totals.

Re-run steps 2–4 anytime the CSVs or SQL change.

