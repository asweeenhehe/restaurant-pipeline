import pandas as pd

def generate_gold_metrics(silver_master_table: pd.DataFrame) -> dict[str, pd.DataFrame]:
    # Ensure date columns are properly parsed if needed
    df = silver_master_table.copy()

    # --- Average Order Value per Store ---
    avg_order_value = (
        df.groupby("store_id", as_index=False)
        .agg(avg_order_value=("order_total", "mean"))
        .sort_values("avg_order_value", ascending=False)
    )

    # --- Support Tickets per Order ---
    tickets_per_order = (
        df.groupby("order_id", as_index=False)
        .agg(ticket_count=("ticket_id", "nunique"))
        .sort_values("ticket_count", ascending=False)
    )

    # --- Store-level Summary (Revenue, Orders, Tickets) ---
    store_metrics = (
        df.groupby("store_id", as_index=False)
        .agg(
            total_revenue=("order_total", "sum"),
            total_orders=("order_id", "nunique"),
            total_tickets=("ticket_id", "nunique"),
        )
    )
    store_metrics["avg_order_value"] = store_metrics["total_revenue"] / store_metrics["total_orders"]

    return {
        "gold_store_metrics": store_metrics,
        "gold_avg_order_value": avg_order_value,
        "gold_tickets_per_order": tickets_per_order,
    }