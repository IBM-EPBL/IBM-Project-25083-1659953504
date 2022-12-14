import requests
from decouple import config
NEWS_API_KEY = config('NEWS_API_KEY')
COUNTRY = 'in'


def get_latest_news():
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']

def getCategory(category):
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&category={category}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']


def searchNews(text):
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&q={text}&apiKey={NEWS_API_KEY}').json()
    print(news_data)
    return news_data['articles']