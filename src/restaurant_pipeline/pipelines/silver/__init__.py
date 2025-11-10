from kedro.pipeline import Pipeline, node
from .nodes import clean_and_transform_data

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=clean_and_transform_data,
            inputs=dict(
                customers="raw_customers",
                orders="raw_orders",
                items="raw_items",
                products="raw_products",
                stores="raw_stores",
                suppliers="raw_suppliers",
                tickets="support_tickets_raw"
            ),
            outputs="silver_master_table",
            name="clean_and_transform_node"
        )
    ])