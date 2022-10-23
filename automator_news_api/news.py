import requests
import creds
from datetime import date

API_KEY = creds.API_KEY
URL = ('https://newsapi.org/v2/top-headlines?')
today = date.today()

def get_articles_by_category():
    print(f"\nGet Top Headlines Published Today! {today} ")
    print("\nChoose a Category from: Business | Entertainment | General | Health | Science | Sports | Technology")
    category = input("Category: ").lower()
    print()
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "ph",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "ph",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)
    articles = response.json()['articles']
    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

if __name__ == "__main__":
    get_articles_by_category()
    print(f"Successfully retrieved top headlines today!\n")

