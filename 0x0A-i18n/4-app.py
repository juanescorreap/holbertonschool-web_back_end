#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import *
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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
    return render_template('4-index.html')


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


if __name__ == "__main__":
    app.run()
