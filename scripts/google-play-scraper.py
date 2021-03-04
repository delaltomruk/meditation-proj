"""
See: https://pypi.org/project/google-play-scraper/
"""


from google_play_scraper import Sort, reviews_all
import json

result = reviews_all(
    'app.meditasyon',
    sleep_milliseconds=0, # defaults to 0
    lang='tr', # defaults to 'en'
    country='tr', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)

print(result)