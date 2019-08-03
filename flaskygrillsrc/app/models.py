from app import db


class Restaurant(db.Model):
    """This class represents the restaurants table."""

    __tablename__ = "restaurants"

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(255))
    date_created    = db.Column(db.DateTime, default = db.func.current_timestamp())
    date_updated    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name=name):
        """Initialized with the name of the restaurant"""
        self.name = name

    def save(self):
        db.session.add(self)
        db.commit()

    def delete(self):
        db.session.remove(self)
        db.commit()
    
    @staticmethod
    def get_all(self):
        return Restaurant.query.all()

    def __repr__(self):
        return "restaurant name: %s",self.name
    

