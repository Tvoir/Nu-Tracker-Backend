from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from models import db, UserModel, CalorieIntakeModel, MacroModel

import os


# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = f'{SQLALCHEMY_DATABASE_URI}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iabhwbwp:OkEpTyalmN5WrMbJT5LeFbcKPtuz8amd@kashin.db.elephantsql.com/iabhwbwp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initialize Database

db.init_app(app)
migrate = Migrate(app, db)

# Initialize Marshmallow
ma = Marshmallow

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Test Route for Postman; delete later
@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'msg': 'Test success'})