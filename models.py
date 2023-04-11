from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


user_club = db.Table(
    'user_club',
    db.Column('user_id', db.Integer,
            db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('club_id', db.Integer,
            db.ForeignKey('club.club_id'), primary_key=True)
)
