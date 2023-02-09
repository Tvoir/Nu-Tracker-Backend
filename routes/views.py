from flask import Blueprint, render_template
#blueprint is basically roots and url's for the app

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")