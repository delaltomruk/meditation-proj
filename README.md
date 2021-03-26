# meditation-proj

The goal of this project is to gain insights on different factors that would affect a meditative state and understand how current meditation apps can overcome these challenges. 

In the improved version, an interface where the user can input different variables and decide on their optimum meditation practice will be implemented.

## Data Collection (Web Crawling)

Collected the following data from different social media websites (tweaked some web scrapers, see  **Code and Resources Used**):

### Twitter
    - Based on hashtags: meditation, meditopia, yoga
### Reddit
    - Subreddits: 'Meditation', 'Buddhism', 'Mindfulness', 'ZenHabits', 'yoga', 'Meditopia'
### Eksi Sozluk
    - Entries: meditasyon, yoga, meditopia
### Apple Store
    - Calm: Turkey and the US
    - Meditopia: Turkey and the US
### Google Play Store
    - Calm: Turkey and the US
    - Meditopia: Turkey and the US

## Data Cleaning

After data collection, we've cleaned it up to make it easily usable. The following changes were made: 
- We first created the json tables as we failed to read the json files directly to pandas DataFrames by pandas functions while normalizing.
- Instead, we used pandas.json_normalize() at the the tables to create the DataFrames. 
- We inspected the DataFrames, and found review date, review itself, and review rating (if it had any) to be useful for our semantic analysis. Thus, we dropped rest of the columns such as the reviewer_ID, and other attributes of the reviews. 
- Then we converted the DataFrames to csv files for further data visualization and analysis. 

## Exploratory Data Analysis (EDA)

Implemented sentiment analysis.

## Code and Resources Used

Python Version: 3.7

Packages: selenium, json, beautiful soup

Scraper: 
- Eksi Sozluk: https://github.com/bariscimen/EksiSozlukEntryCrawler
- Google Play Store: https://pypi.org/project/google-play-scraper/
- App Store: https://pypi.org/project/app-store-scraper/
