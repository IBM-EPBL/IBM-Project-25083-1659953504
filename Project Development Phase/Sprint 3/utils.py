import requests
from decouple import config
NEWS_API_KEY = config('NEWS_API_KEY')
# COUNTRY = 'in'


def get_latest_news():
    news_data = requests.get(f'https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&country=in&language=en').json()
    return news_data['results']

def getCategory(category):
    news_data = requests.get(f'https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&category={category}&country=in&language=en').json()
    return news_data['results']


def searchNews(text):
    news_data = requests.get(f'https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&q={text}&country=in&language=en').json()
    return news_data['results']