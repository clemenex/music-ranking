import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_kworb_charts():
    url = "https://kworb.net/spotify/country/global_daily.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 11:
            try:
                position = cols[0].text.strip()
                artist_title = cols[2].text.strip()
                days = cols[4].text.strip()
                total_streams = cols[10].text.strip()

                # Split artist and title
                if " - " in artist_title:
                    artist, title = artist_title.split(" - ", 1)
                else:
                    artist, title = artist_title, "N/A"

                data.append({
                    "Position": position,
                    "Artist": artist.strip(),
                    "Title": title.strip(),
                    "Days": days,
                    "Total Streams": total_streams
                })
            except Exception as e:
                print(f"Skipping row due to error: {e}")

    df = pd.DataFrame(data)
    df.to_csv("kworb_charts.csv", index=False)
    print("Scraping complete! Data saved to 'kworb_charts.csv'.")
