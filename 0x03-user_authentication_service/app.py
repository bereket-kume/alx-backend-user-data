#!/usr/bin/env python3
"""
Basic Falsk app
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def basic_app():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email=email, password=password):
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=["GET"])
def profile() -> str:
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)
    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
