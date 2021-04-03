from flask import Flask, render_template, request

# TODO: create new Flask app
app = None


@app.route("/")
def main_page():
    # TODO: return index.html
    return None


# TODO: Add route for sign up
def sign_up():
    # TODO: get user input from request
    email = None
    username = None
    password = None

    if not user_exists(email=email, username=username, password=password):
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"


def user_exists(email, username, password):
    # TODO: check for user if exists
    return None