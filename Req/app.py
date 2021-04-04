from flask import Flask, render_template, request

# TODO: create new Flask app
app = Flask(__name__)

global user
user = 'samar'


@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template("index.html")


# TODO: Add route for sign up
@app.route("/index", methods=['POST'])
def sign_up():
    # TODO: get user input from request

    email = request.form['email']
    username = request.form['username']
    password = request.form['password']


    if not user_exists(email=email, username=username, password=password):
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"


def user_exists(email, username, password):
    # TODO: check for user if exists
    if username == user:
        return True
    else:
        return False
