# from crypt import methods
import json
from flask import Flask , request ,render_template , redirect , url_for
# from flask_cors import CORS
from DB_op import signinusersdb  ,signupusersdb ;

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



# Add this part
@app.route('/news')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)

@app.route('/category/<category>')
def newsCategory(category):
    news_articles = getCategory(category)
    return render_template("news.html", news_articles=news_articles)


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
    app.run(debug=1)    