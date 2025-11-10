import pandas as pd
import matplotlib.pyplot as plt

# Load gold data
df = pd.read_csv("data/03_primary/gold_store_metrics.csv")

print("\n=== GOLD METRICS OVERVIEW ===")
print(df.head(), "\n")

# Sort by revenue
df = df.sort_values("total_revenue", ascending=False)

# Plot 1 — Total Revenue by Store
plt.figure(figsize=(10,5))
plt.bar(df["store_name"], df["total_revenue"])
plt.title("Total Revenue by Store")
plt.xlabel("Store Name")
plt.ylabel("Total Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2 — Average Order Value by Store
plt.figure(figsize=(10,5))
plt.bar(df["store_name"], df["average_order_value"], color="orange")
plt.title("Average Order Value by Store")
plt.xlabel("Store Name")
plt.ylabel("Average Order Value (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3 — Total Tickets by Store
plt.figure(figsize=(10,5))
plt.bar(df["store_name"], df["total_tickets"], color="green")
plt.title("Total Tickets by Store")
plt.xlabel("Store Name")
plt.ylabel("Tickets Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()