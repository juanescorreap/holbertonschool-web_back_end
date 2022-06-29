#!/usr/bin/env python3
"""
Basic Flask app that has a single GET route
"""
from flask import Flask, jsonify, abort, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    """
    Method that returns a JSON welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user(email: str, password: str):
    """
    Method that registers a new user if it doesnt exist
    or returns a warning message if it does
    """
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
