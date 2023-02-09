#blueprint is basically roots and url's for the app
from flask import Blueprint, render_template

macros = Blueprint('macros', __name__)

@macros.route('/')
def home():
    return render_template("home.html")