import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_lastfm_charts():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    url = "https://www.last.fm/charts"
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    chart_list = soup.find_all("tr", class_="globalchart-item")

    all_tracks = []
    for row in chart_list:
        rank = row.find("td", class_="globalchart-rank").text.strip()

        track_td = row.find("td", class_="globalchart-name")
        title = track_td.find("a", class_="link-block-target").text.strip() if track_td else "N/A"

        artist_td = row.find("td", class_="globalchart-track-artist-name")
        artist = artist_td.find("a").text.strip() if artist_td else "N/A"

        all_tracks.append({
            "Rank": rank,
            "Title": title,
            "Artist": artist
        })

    df = pd.DataFrame(all_tracks)
    df.to_csv("lastfm_charts.csv", index=False)
    print("Scraping complete! Data saved to 'lastfm_charts.csv'.")
