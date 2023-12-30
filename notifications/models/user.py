import datetime
from notifications import db


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"User('{self.title}','{self.text}')"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date': self.date_created
        }