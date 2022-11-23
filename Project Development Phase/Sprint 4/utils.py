import requests
from decouple import config
NEWS_API_KEY = config('NEWS_API_KEY')
# COUNTRY = 'in'


def get_latest_news():
    news_data = requests.get(f'https://newsapi.org/v2//top-headlines?country=us&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']

def getCategory(category):
    news_data = requests.get(f'https://newsapi.org/v2//top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']


def searchNews(text):
    news_data = requests.get(f'https://newsapi.org/v2/everything?q={text}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']