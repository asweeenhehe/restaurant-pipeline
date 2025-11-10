from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_raw_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_raw_data,
            inputs=[
                "raw_customers",
                "raw_items",
                "raw_orders",
                "raw_products",
                "raw_stores",
                "raw_suppliers",
                "support_tickets_raw"
            ],
            outputs="bronze_preview",
            name="load_raw_data_node"
        )
    ])