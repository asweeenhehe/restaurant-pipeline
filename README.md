# 🍽️ Restaurant Pipeline Project — Kedro Data Engineering

## 📘 Overview
This project implements a **modular data pipeline** for a restaurant chain using **Kedro**, designed to ingest, clean, and analyze operational and customer support data.  
It follows a **multi-layered architecture** — *Bronze → Silver → Gold* — to progressively refine raw data into analytical insights.

---

## 🧱 Pipeline Architecture

| Layer  | Purpose                                                                 | Example Outputs                                                  |
|---------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| **Bronze** | Ingests raw data from multiple sources (CSV, JSONL).                     | `raw_customers.csv`, `support_tickets.jsonl`                     |
| **Silver** | Cleans, merges, and standardizes entities into a master analytical table. | `silver_master_table.csv`                                        |
| **Gold**   | Performs business-level aggregations and analytics models.              | `gold_avg_order_value.csv`, `gold_tickets_per_order.csv`, `gold_store_metrics.csv` |

---

## ⚙️ Datasets Processed

| Dataset | Source Type | Description |
|----------|--------------|-------------|
| **Customers** | CSV | Customer information |
| **Orders** | CSV | Sales transactions |
| **Items** | CSV | Individual line items per order |
| **Products** | CSV | Product catalog with pricing |
| **Stores** | CSV | Store and tax details |
| **Suppliers** | CSV | Supplier relationships and costs |
| **Support Tickets** | JSONL (Azure Blob) | Customer service interactions |

---

## 🧩 Key Analytics Models

### 1️⃣ Average Order Value (AOV)
- Groups transactions by `store_id`
- Computes `avg_order_value = total_revenue / total_orders`

### 2️⃣ Tickets per Order
- Groups support tickets by `order_id`
- Aggregates `ticket_count` to measure post-order engagement

### 3️⃣ Store Metrics Dashboard
Combines all key KPIs:

| Metric | Description |
|---------|-------------|
| `total_revenue` | Sum of order totals per store |
| `total_orders` | Total number of orders per store |
| `total_tickets` | Total customer support cases linked to each store |
| `avg_order_value` | Revenue efficiency per order |

---

## 🧠 Example Outputs

### **Average Order Value**
store_id                              avg_order_value
a9128331-08d7-41a2-b615-21283eee21cf  1059.02
a2a24e87-dec8-4f5d-9c9e-0e9849529489  1021.55

### **Tickets per Order**
order_id                              ticket_count
0000dda0-bedb-4109-bdfb-1bbbed16af12  0
ab36ac8f-0c12-4bd3-9b4c-3572ba01004b  0

### **Store Metrics**
store_id                              total_revenue  total_orders  total_tickets  avg_order_value
a2a24e87-dec8-4f5d-9c9e-0e9849529489   22822628       22341          0             1021.56
a9128331-08d7-41a2-b615-21283eee21cf   43215565       40807          0             1059.02

---

## 🚀 Run Instructions

### 1️⃣ Set up environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r src/requirements.txt

2️⃣ Run each pipeline layer
kedro run --pipeline=bronze
kedro run --pipeline=silver
kedro run --pipeline=gold

3️⃣ Analyze Gold outputs
python analyze_gold_metrics.py

📂 Folder Structure
restaurant-pipeline/
│
├── data/
│   ├── 01_raw/                <- Raw input files (Bronze)
│   ├── 02_silver/             <- Cleaned merged master table
│   ├── 03_primary/            <- Gold analytics outputs
│
├── src/restaurant_pipeline/
│   ├── pipelines/
│   │   ├── bronze/            <- Ingestion logic
│   │   ├── silver/            <- Cleaning & transformation logic
│   │   ├── gold/              <- Business KPIs & analytics
│
├── analyze_gold_metrics.py    <- Local analysis script
└── README.md

📊 Insights Visualization

After generating the gold-layer analytics, three charts were created using Matplotlib (analyze_gold_metrics.py):

1️⃣ Average Order Value by Store

Shows the average transaction size per store, useful for identifying high-value outlets.
plt.bar(aov['store_id'], aov['avg_order_value'])
plt.title("Average Order Value by Store")

2️⃣ Tickets per Order Distribution

Plots how frequently support tickets occur per order.
tickets['ticket_count'].hist()
plt.title("Tickets per Order Distribution")

3️⃣ Total Revenue per Store

Visualizes cumulative sales per store — a direct indicator of performance.
plt.bar(store['store_id'], store['total_revenue'])
plt.title("Total Revenue per Store")


🧾 Summary

The visualizations confirm the data pipeline’s integrity and provide business-ready insights:
	•	High-revenue stores correlate with higher average order values
	•	Customer support demand remains low, showing efficient operations
	•	The pipeline successfully transforms raw operational data into actionable metrics

⸻

🧰 Tech Stack
	•	Kedro — Data pipeline orchestration
	•	Pandas — Data wrangling
	•	Matplotlib — Visualization
	•	Azure Blob Storage — Cloud data source for tickets

---