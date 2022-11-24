# from crypt import methods
import json
from flask import Flask , request ,render_template , redirect , url_for
# from flask_cors import CORS
from DB_op import signinusersdb  ,signupusersdb  ,addNewsDb ,get_savedNews;

from utils import get_latest_news , getCategory,searchNews


app = Flask(__name__,template_folder = 'templates')


class sessionobj:
    def __init__(self,email):
        self.email = email

@app.route('/')
def welcome():
    return render_template("login.html")

@app.route('/signinusers',methods=['POST'])
def signinusers():
    value = signinusersdb(json.loads(request.get_data())['id'],json.loads(request.get_data())['password'])
    return value


@app.route('/signupusers',methods=['POST'])
def signupusers():
    value = signupusersdb(json.loads(request.get_data())['name'],json.loads(request.get_data())['email'],json.loads(request.get_data())['password'])
    # print(json.loads(request.get_data()))
    return value


@app.route('/addNews',methods=['POST'])
def addNews():
    value = addNewsDb(json.loads(request.get_data())['id'],json.loads(request.get_data())['newsLink'],json.loads(request.get_data())['newsTitle'],json.loads(request.get_data())['newsImage'],json.loads(request.get_data())['newsDescrp'])
    return value

@app.route('/news')
def news_headlines():
    news_articles = get_latest_news()
    # print(news_articles)
    return render_template("news.html", news_articles=news_articles)
    # return news_articles

@app.route('/category/<category>')
def newsCategory(category):
    news_articles = getCategory(category)
    return render_template("news.html", news_articles=news_articles)


@app.route('/savedNews/<id>', methods=['GET', 'POST'])
def showSavedNews(id):
    news_articles = get_savedNews(id)
    return render_template("savedNews.html", news_articles=news_articles)


@app.route('/search/<text>')
def newsSearch(text):
    news_articles = searchNews(text)
    return render_template("news.html", news_articles=news_articles)

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)    