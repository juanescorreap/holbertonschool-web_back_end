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
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
