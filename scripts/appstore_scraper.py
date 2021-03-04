"""
See: https://pypi.org/project/app-store-scraper/
"""

from app_store_scraper import AppStore
from pprint import pprint

calm = AppStore(country="us", app_name="Cal‪m")
calm.review(how_many=1000)

pprint(calm.reviews)
