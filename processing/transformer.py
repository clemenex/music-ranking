import pandas as pd

def process_and_merge_data(lastfm_path="lastfm_charts.csv", kworb_path="kworb_charts.csv"):
    # Load both datasets
    lastfm_df = pd.read_csv(lastfm_path)
    kworb_df = pd.read_csv(kworb_path)

    # Clean up column names
    lastfm_df.columns = lastfm_df.columns.str.strip().str.lower().str.replace(" ", "_")
    kworb_df.columns = kworb_df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Make sure Artist and Title are standardized
    lastfm_df["artist"] = lastfm_df["artist"].str.strip().str.lower()
    lastfm_df["title"] = lastfm_df["title"].str.strip().str.lower()

    kworb_df["artist"] = kworb_df["artist"].str.strip().str.lower()
    kworb_df["title"] = kworb_df["title"].str.strip().str.lower()

    # Merge on artist + title
    merged_df = pd.merge(lastfm_df, kworb_df, on=["artist", "title"], how="inner", suffixes=('_lastfm', '_kworb'))

    # Save to CSV
    merged_df.to_csv("merged_charts.csv", index=False)
    print("Merged data saved to 'merged_charts.csv'")
    return merged_df
