import pandas as pd

def load_raw_data(raw_customers, raw_items, raw_orders, raw_products, raw_stores, raw_suppliers, support_tickets_raw):
    """Combine all raw sources into a dictionary for inspection."""
    return {
        "customers": raw_customers.head(),
        "items": raw_items.head(),
        "orders": raw_orders.head(),
        "products": raw_products.head(),
        "stores": raw_stores.head(),
        "suppliers": raw_suppliers.head(),
        "tickets": support_tickets_raw.head()
    }