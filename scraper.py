import pandas as pd
from lastfm_scraper import scrape_lastfm_charts
from kworb_scraper import scrape_kworb_charts

# Run the Billboard scraper
print("Running LastFM scraper...")
scrape_lastfm_charts()

# Run the Kworb scraper
print("Running Kworb scraper...")
scrape_kworb_charts()

# Load the data
lastfm_df = pd.read_csv("lastfm_charts.csv")
kworb_df = pd.read_csv("kworb_charts.csv")

# Merge the dataframes on 'song_name' (assumes the song names match)
merged_df = pd.merge(lastfm_df, kworb_df, on="Title", suffixes=('_billboard', '_kworb'))

# Save the merged dataframe to CSV
merged_df.to_csv("hot100_comparison.csv", index=False)

print("Comparison complete! Data saved to 'hot100_comparison.csv'.")