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

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iabhwbwp:dKqGPwIQB2nkdABmE1mHCjqQSGnma5Ci@kashin.db.elephantsql.com/iabhwbwp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initialize Database

db.init_app(app)
migrate = Migrate(app, db)

# Initialize Marshmallow
ma = Marshmallow

#importing pathways
from views import views

#url prefix is how you access the blueprint
app.register_blueprint(views, url_prefix='/')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Test Route for Postman; delete later
@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'msg': 'Test success'})