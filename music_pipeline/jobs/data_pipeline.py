from dagster import job, op, get_dagster_logger
import pandas as pd
import os

@op
def load_lastfm_csv() -> pd.DataFrame:
    df = pd.read_csv("lastfm_artists.csv")
    return df

@op
def load_kworb_csv() -> pd.DataFrame:
    df = pd.read_csv("kworb_charts.csv")
    return df
@op
def merge_and_clean(lastfm_df: pd.DataFrame, kworb_df: pd.DataFrame) -> pd.DataFrame:
    for df in [lastfm_df, kworb_df]:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    kworb_agg = kworb_df.groupby("artist").agg(
        kworb_song_count=("title", "count"),
        kworb_song_titles=("title", lambda titles: ", ".join(sorted(set(titles))))
    ).reset_index()

    merged_df = pd.merge(lastfm_df, kworb_agg, on="artist", how="left")

    merged_df["kworb_song_count"] = merged_df["kworb_song_count"].fillna(0).astype(int)
    merged_df["kworb_song_titles"] = merged_df["kworb_song_titles"].fillna("")

    assert not merged_df.empty, "Merged DataFrame is empty!"

    return merged_df

@op
def save_merged_data(df: pd.DataFrame):
    df.to_csv("merged_charts.csv", index=False)
    get_dagster_logger().info("Saved merged data to 'merged_charts.csv'")

@job
def music_data_pipeline():
    lastfm_df = load_lastfm_csv()
    kworb_df = load_kworb_csv()
    merged_df = merge_and_clean(lastfm_df, kworb_df)
    save_merged_data(merged_df)
