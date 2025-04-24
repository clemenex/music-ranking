from dagster import job, op, In, Out, get_dagster_logger
import pandas as pd

@op
def load_lastfm_csv() -> pd.DataFrame:
    df = pd.read_csv("lastfm_charts.csv")
    return df

@op
def load_kworb_csv() -> pd.DataFrame:
    df = pd.read_csv("kworb_charts.csv")
    return df

@op
def merge_and_clean(lastfm_df: pd.DataFrame, kworb_df: pd.DataFrame) -> pd.DataFrame:
    # Clean and merge
    for df in [lastfm_df, kworb_df]:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        df["artist"] = df["artist"].str.strip().str.lower()
        df["title"] = df["title"].str.strip().str.lower()

    merged = pd.merge(lastfm_df, kworb_df, on=["artist", "title"], how="inner", suffixes=('_lastfm', '_kworb'))

    # Basic data quality check
    assert not merged.empty, "Merged DataFrame is empty!"

    return merged

@op
def save_merged_data(df: pd.DataFrame):
    df.to_csv("merged_charts.csv", index=False)
    get_dagster_logger().info("Saved merged data to 'merged_charts.csv'")

@job
def music_data_pipeline():
    save_merged_data(merge_and_clean(load_lastfm_csv(), load_kworb_csv()))
