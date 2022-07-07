#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    """
    Basic method to render
    the 0-index.html template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
