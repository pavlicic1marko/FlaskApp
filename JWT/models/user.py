from JWT import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)

    def __repr__(self):
        return f"User('{self.title}','{self.text}')"
