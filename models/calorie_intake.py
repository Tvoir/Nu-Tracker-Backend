from ..app import db

class CalorieIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    food = db.Column(db.String(80), nullable=False)
    calories = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<CalorieIntake %r>' % self.id