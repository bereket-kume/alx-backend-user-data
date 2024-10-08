#!/usr/bin/env python3
"""
Session Auth
"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
from api.v1.auth.session_auth import SessionAuth
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_login():
    """
    method to display login session
    """
    auth = SessionAuth()
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        users = None
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()
    response = jsonify(user_json)
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)
    return response


@app_views.route(
    "/auth_session/logout",
    methods=["DELETE"],
    strict_slashes=False
)
def session_logout():
    """
    method used for session logout
    """
    auth = SessionAuth()
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
