#!/usr/bin/env python3
"""
Flask view that handles all routes for the Session authentication
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Handles user login endpoint
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            json_user = jsonify(user.to_json())
            json_user.set_cookie(os.getenv('SESSION_NAME'), session_id)
            return json_user
        else:
           return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """
    Handles user logout endpoint
    """
    from api.v1.app import auth
    logout_request = auth.destroy_session(request)
    if logout_request is False:
        abort(404)
    else:
        return jsonify({}), 200
