import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_weekly_charts(pages=4):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    base_url = "https://www.last.fm/charts/weekly?page="
    all_artists = []

    for page_num in range(1, pages + 1):
        url = f"{base_url}{page_num}"
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        chart_rows = soup.find_all("tr", class_="weeklychart-item")

        for row in chart_rows:
            position = row.find("td", class_="weeklychart-rank").text.strip()

            name_td = row.find("td", class_="weeklychart-name")
            name_link = name_td.find("a", class_="link-block-target")
            artist_name = name_link.text.strip() if name_link else "N/A"

            listeners_td = row.find("td", class_="weeklychart-listeners")
            listeners = listeners_td.text.strip() if listeners_td else "N/A"

            all_artists.append({
                "Position": position,
                "Artist": artist_name,
                "Listeners": listeners
            })

    driver.quit()

    df = pd.DataFrame(all_artists)
    df.to_csv("lastfm_artists.csv", index=False)
    print("Scraping complete! Data saved to 'lastfm_artists.csv'.")