from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize Database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Test Route for Postman; delete later
@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'msg': 'Test success'})