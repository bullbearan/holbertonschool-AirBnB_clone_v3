#!/usr/bin/python3
""" This is a line of text """
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from os import environ


app = Flask(__name__)
CORS(app, orgins='0.0.0.0')
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(e):
    """json 404 page"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def close_db(exception):
    """ closes the session """
    storage.close()


if __name__ == "__main__":
    host = environ.get("HBNB_API_HOST", "0.0.0.0")
    port = environ.get("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
