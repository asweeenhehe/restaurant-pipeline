import pandas as pd

def clean_and_transform_data(customers, orders, items, products, stores, suppliers, tickets):
    # --- Standardize column names ---
    def clean_columns(df):
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        return df

    dfs = [customers, orders, items, products, stores, suppliers, tickets]
    customers, orders, items, products, stores, suppliers, tickets = [clean_columns(df) for df in dfs]

    # --- Rename IDs and name columns for consistency ---
    orders = orders.rename(columns={"id": "order_id", "customer": "customer_id"})
    customers = customers.rename(columns={"id": "customer_id", "name": "customer_name"})
    stores = stores.rename(columns={"id": "store_id", "name": "store_name"})
    suppliers = suppliers.rename(columns={"id": "supplier_id", "name": "supplier_name"})
    products = products.rename(columns={"name": "product_name"})
    tickets = tickets.rename(columns={"customer_external_id": "customer_id"})

    # --- Normalize data types for join keys (convert to string to avoid merge errors) ---
    for df, cols in [
        (customers, ["customer_id"]),
        (orders, ["order_id", "customer_id", "store_id"]),
        (items, ["order_id", "sku"]),
        (tickets, ["order_id", "customer_id"]),
        (products, ["sku"]),
        (suppliers, ["sku"]),
    ]:
        for c in cols:
            if c in df.columns:
                df[c] = df[c].astype("string")

    # --- Basic cleaning ---
    customers = customers.drop_duplicates()
    products = products.drop_duplicates().fillna({"price": 0})
    orders = orders.drop_duplicates().fillna({"status": "Pending"})

    # --- Merge all core datasets ---
    merged = (
        orders
        .merge(items, on="order_id", how="left")
        .merge(products, on="sku", how="left")
        .merge(customers, on="customer_id", how="left")
        .merge(stores, on="store_id", how="left")
        .merge(suppliers, on="sku", how="left")
    )

    # --- Merge ticket details (adds ticket_id and related fields) ---
    merged = merged.merge(tickets, on=["customer_id", "order_id"], how="left")

    # --- Add ticket count per order ---
    if "order_id" in tickets.columns:
        ticket_count = tickets.groupby("order_id", dropna=False).size().reset_index(name="ticket_count")
        ticket_count["order_id"] = ticket_count["order_id"].astype("string")
        merged = merged.merge(ticket_count, on="order_id", how="left")
    else:
        merged["ticket_count"] = 0

    # --- Final cleanup (only fill descriptive columns) ---
    text_cols = [
        "customer_name", "product_name", "store_name", "supplier_name",
        "description", "status", "priority", "category", "subject", "body", "sentiment"
    ]
    for col in text_cols:
        if col in merged.columns:
            merged[col] = merged[col].fillna("Unknown")

    # --- Safe duplicate removal (only if 'item_id' exists) ---
    if "item_id" in merged.columns:
        merged = merged.drop_duplicates(subset=["order_id", "item_id"], keep="first")
    else:
        merged = merged.drop_duplicates(subset=["order_id"], keep="first")

    return merged