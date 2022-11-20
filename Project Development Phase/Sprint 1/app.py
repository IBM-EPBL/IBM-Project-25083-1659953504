# from crypt import methods
from flask import *
from flask_cors import CORS
from DB_op import *;


app = Flask(__name__,template_folder = 'templates')





class sessionobj:
    def __init__(self,email):
        self.email = email

@app.route('/')
def welcome():
    return render_template("login.html")

# @app.route('/signinusers',methods=['POST'])
# def signinusers():
#     value = signinusersdb(json.loads(request.get_data())['id'],json.loads(request.get_data())['password'])
#     print(json.loads(request.get_data()))
#     return value

# @app.route('/signupusers',methods=['POST'])
# def signupusers():
#     value = signupusersdb(json.loads(request.get_data())['name'],json.loads(request.get_data())['email'],json.loads(request.get_data())['password'])
#     print(json.loads(request.get_data()))
#     return value


@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)    