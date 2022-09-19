#!/usr/bin/python3
""" A mold for app_view """ 
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from flask import Flask
from api.v1.views.index import *
from api.v1.views.states import *
