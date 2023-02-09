from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db =SQLAlchemy()

class UserModel(db.Model, UserMixin):

    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    #calorieNotes = db.relationship('CalorieIntakeModel')
    #calorieMacros = db.relationship('MacroModel')

    def __repr__(self):
        return '<User %r>' % self.username

class CalorieIntakeModel(db.Model):

    __tablename__ = 'calorie_table'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    food = db.Column(db.String(80), nullable=False)
    calories = db.Column(db.Float, nullable=False)
    #userModel_id = db.Column(db.Integer. db.ForeignKey('UserModel.id'))

    def __repr__(self):
        return '<CalorieIntake %r>' % self.id

class MacroModel(db.Model):

    __tablename__ = 'macro_tabel'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    #userModel_id = db.Column(db.Interger. db.ForeignKey('UserModel.id'))

    def __repr__(self):
        return '<Macro %r>' % self.id