# Goodreads Genre-Based Book Scraper

## 📌 Overview
This project gathers artist popularity data from Last.fm and song performance data from Kworb.net, then merges the results to identify artists whose songs are currently charting on Kworb. It enables cross-platform musical trend analysis by showing which Last.fm chart-topping artists also have popular songs across global digital platforms.

The project aims to:

- Scrape weekly artist chart rankings from Last.fm

- Scrape daily/weekly song performance from Kworb.net

- Merge both datasets and count how many songs from each artist are currently charting

The scraped data is saved into a CSV file for further analysis. The types of data gathered are all relevant to building a much larger project later on.

## 🌐 Website Selection
### Last.fm
URL: https://www.last.fm/charts/weekly?page=1

I specifically scrape artist rankings instead of song rankings due to better breadth (more unique artists over top 20 songs).
This ensures more overlap when matching with songs from Kworb.

### Kworb.net
URL: https://kworb.net/spotify/country/global_daily.html
Kworb is a public aggregator of music charts across Spotify, Apple Music, iTunes, etc.

I scraped this website for the top-performing songs and their respective artists.

## ⚙️ Technologies Used
- **Python**
- **Selenium**
- **BeautifulSoup**
- **Pandas**
- **Dagster**

## 🔬 Methodology

# Web Scraping Methodology Flow Diagram
For better reference, kindly refer to the `book.py` file to see the actual code.

```plaintext
+------------------------------------------+
|      1. Scrape Last.fm Artist Chart      |
| - Visit weekly chart pages               |
| - Extract artist names                   |
| - Append all artist entries to list      |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
|       2. Scrape Kworb.net Song Chart     |
| - Extract song name and artist name      |
| - Save all song-artist entries           |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
|         3. Data Cleaning and Merging     |
|           via Dagster Data Pipeline      |
| - Normalize artist names (e.g., case)    |
| - Merge dataframes based on artist       |
| - Count songs per Last.fm artist         |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
|      4. Save Merged Data and Summary     |
| - Save CSVs for artists, songs, and      |
|   merged intersection                    |
| - Output summary insights to console     |
+------------------------------------------+
```

## 📋 Challenges and Limitations
### 1️⃣  Data Intersection
- Not all artists from Last.fm have charting songs on Kworb, and vice versa.
- Merging is not exact, since artist names may slightly differ in formatting (e.g., "The Weeknd" vs "Weeknd"). This was solved under the data transformation pipeline, wherein I did basic normalization such as stripping and lowering.

### 2️⃣ Data Depth
- Last.fm only exposes top 100 artists per page. 

## ✅ Ethical Considerations
The project follows the rules and guidelines laid down by the website (https://kworb.net/robots.txt), (https://last.fm/robots.txt). No personal data such as `/user/*/library*` or specific song data from `/search` was scraped in order to avoid breaking the scraping guidelines.

- The project avoids scraping any personal or sensitive information and only collects publicly available data such as song titles, artists, listeners, and postion/ranking.
- Personal details such as user reviews, profile data, or private messages are not scraped. The script is focused solely on general artist and song data from the public chart pages.
- The script uses a delay (time.sleep(3)) between each request to reduce the load on the server and mimic more human-like browsing behavior. This prevents overwhelming the servers with too many rapid requests. By scraping at a controlled rate, the script aims to prevent affecting the user experience of others and to avoid violating terms related to server load or overuse.

## 📁 Output and Result
For the project's output and result, kindly refer and open the csv file: `kworb_charts.csv` and `lastfm_artists.csv`. The files can be viewed by itself here on Github or may also be downloadable.

## 🚀 How to Run the Scraper
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Script
Execute the following command:
```sh
python scraper.py
```


## 🤝 Contributions
Feel free to fork the repo, submit PRs, or open issues! 😊