#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import *
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Class used with the configuration
    for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""
Using the class to configure the app
"""


@app.route('/')
def main():
    """
    Basic method to render
    the 0-index.html template
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    Method to select the best matching language
    """
    locale = request.args.get('locale')
    available_languages = app.config['LANGUAGES']
    if locale in available_languages:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Method that returns the user id from
    the mock database if present
    """
    try:
        user_id = request.args.get('login_as')
        return user_id[int(user_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """
    Method to find a user and set it
    as global in flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
