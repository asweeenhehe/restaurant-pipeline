import pandas as pd
import matplotlib.pyplot as plt
import os

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# Load gold data
df = pd.read_csv("data/03_primary/gold_store_metrics.csv")

print("\n=== GOLD METRICS OVERVIEW ===")
print(df.head(), "\n")

# Sort by revenue for consistent order
df = df.sort_values("total_revenue", ascending=False)

# Shorten store_id for better readability in plots
df["store_short"] = df["store_id"].str[:8]

# --- Plot 1: Total Revenue by Store ---
plt.figure(figsize=(10, 5))
plt.bar(df["store_short"], df["total_revenue"], color="#1f77b4")
plt.title("Total Revenue by Store")
plt.xlabel("Store ID (short)")
plt.ylabel("Total Revenue (€)")
plt.tight_layout()
plt.savefig("images/total_revenue_by_store.png")
plt.close()

# --- Plot 2: Average Order Value by Store ---
plt.figure(figsize=(10, 5))
plt.bar(df["store_short"], df["avg_order_value"], color="#ff7f0e")
plt.title("Average Order Value (AOV) by Store")
plt.xlabel("Store ID (short)")
plt.ylabel("Average Order Value (€)")
plt.tight_layout()
plt.savefig("images/avg_order_value_by_store.png")
plt.close()

# --- Plot 3: Total Tickets by Store ---
plt.figure(figsize=(10, 5))
plt.bar(df["store_short"], df["total_tickets"], color="#2ca02c")
plt.title("Total Tickets by Store")
plt.xlabel("Store ID (short)")
plt.ylabel("Tickets Count")
plt.tight_layout()
plt.savefig("images/total_tickets_by_store.png")
plt.close()

print("✅ Figures saved successfully to the 'images/' folder.")