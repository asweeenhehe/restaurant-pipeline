from kedro.pipeline import Pipeline, node
from .nodes import generate_gold_metrics

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=generate_gold_metrics,
                inputs="silver_master_table",
                outputs={
                    "gold_store_metrics": "gold_store_metrics",
                    "gold_avg_order_value": "gold_avg_order_value",
                    "gold_tickets_per_order": "gold_tickets_per_order",
                },
                name="generate_gold_metrics_node",
            ),
        ]
    )