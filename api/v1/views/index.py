#!/usr/bin/python3
"""
Status of your API
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """ the object app_views that returns a JSON: status: OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def objects():
    """ Return the number of objects """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    number_objects = {}
    for i in range(len(classes)):
        number_objects[names[i]] = storage.count(classes[i])

    return jsonify(number_objects)
