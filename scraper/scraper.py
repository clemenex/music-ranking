import pandas as pd
from lastfm_scraper import scrape_weekly_charts
from kworb_scraper import scrape_kworb_charts

print("Running LastFM scraper...")
scrape_weekly_charts()

print("Running Kworb scraper...")
scrape_kworb_charts()

lastfm_df = pd.read_csv("lastfm_artists.csv")
kworb_df = pd.read_csv("kworb_charts.csv")