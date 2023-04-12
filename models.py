from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


user_club = db.Table(
    'user_club',
    db.Column('user_id', db.Integer,
            db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('club_id', db.Integer,
            db.ForeignKey('club.club_id'), primary_key=True)
)
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    clubs = db.relationship('Club', secondary=user_club)

    def __init__(self, name: str, password: str, email: str):
        self.name = name
        self.password = password
        self.email = email


class Club(db.Model):
    club_id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String, nullable=False)
    club_description = db.Column(db.String, nullable=False)

    def __init__(self, club_name: str, club_description: str) -> None:
        self.club_name = club_name
        self.club_description = club_description

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    event_description = db.Column(db.String, nullable=False)
    event_location = db.Column(db.String, nullable=False)

    club_id = db.Column(db.Integer, db.ForeignKey(Club.club_id), nullable = False)

    def __init__(self, event_name: str, event_description: str, event_location: str) -> None:
        self.event_name = event_name
        self.event_description = event_description
        self.event_location = event_location
