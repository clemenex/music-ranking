import pandas as pd
from dagster import asset

@asset
def music_data() -> pd.DataFrame:
    df = pd.read_csv("merged_charts.csv")
