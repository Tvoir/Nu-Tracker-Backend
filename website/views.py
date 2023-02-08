from flask import Blueprint
#blueprint is basically roots and url's for the app

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> Test</h1>"