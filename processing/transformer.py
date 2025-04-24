import pandas as pd

def process_and_merge_data(lastfm_path="lastfm_artists.csv", kworb_path="kworb_charts.csv"):
    # Load both datasets
    lastfm_df = pd.read_csv(lastfm_path)
    kworb_df = pd.read_csv(kworb_path)

    # Standardize column names
    lastfm_df.columns = lastfm_df.columns.str.strip().str.lower().str.replace(" ", "_")
    kworb_df.columns = kworb_df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Standardize artist names
    lastfm_df["artist"] = lastfm_df["artist"].str.strip().str.lower()
    kworb_df["artist"] = kworb_df["artist"].str.strip().str.lower()
    kworb_df["title"] = kworb_df["title"].str.strip()

    # Aggregate song count and song titles for each artist from kworb
    kworb_agg = kworb_df.groupby("artist").agg(
        kworb_song_count=("title", "count"),
        kworb_song_titles=("title", lambda titles: ", ".join(sorted(set(titles))))
    ).reset_index()

    # Merge aggregated song data into the Last.fm chart
    merged_df = pd.merge(lastfm_df, kworb_agg, on="artist", how="left")

    # Fill missing values for artists not in Kworb
    merged_df["kworb_song_count"] = merged_df["kworb_song_count"].fillna(0).astype(int)
    merged_df["kworb_song_titles"] = merged_df["kworb_song_titles"].fillna("")

    # Save result
    merged_df.to_csv("merged_artist_kworb_detailed.csv", index=False)
    print("Merged data saved to 'merged_artist_kworb_detailed.csv'")
    return merged_df

process_and_merge_data()