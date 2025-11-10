from kedro.pipeline import Pipeline
from restaurant_pipeline.pipelines import bronze as bronze_pipeline
from restaurant_pipeline.pipelines import silver as silver_pipeline
from restaurant_pipeline.pipelines import gold as gold_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    bronze = bronze_pipeline.create_pipeline()
    silver = silver_pipeline.create_pipeline()
    gold = gold_pipeline.create_pipeline()

    return {
        "__default__": bronze + silver + gold,
        "bronze": bronze,
        "silver": silver,
        "gold": gold,
    }