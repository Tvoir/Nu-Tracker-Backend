#blueprint is basically roots and url's for the app
from flask import Blueprint, render_template

diary = Blueprint('diary', __name__)

@diary.route('/')
def diary():
    return render_template("home.html")