from carMarket import db


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=40), nullable=False)
    last_name = db.Column(db.String(length=40), nullable=False)
    email = db.Column(db.String(length=50))
    gender = db.Column(db.String(length=20))
    ip_address = db.Column(db.String(length=50))

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
