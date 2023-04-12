from models import db, User, Club, user_club, Event

class ClubRepository:

    def join_club(self, user_id, club_id):
        join = user_club(user_id, club_id)
        db.session.add(join)
        db.session.commit()
        return join

    def create_event(self, event_name, event_description, event_location):
        create = Event(event_name, event_description, event_location)
        db.session.add(create)
        db.session.commit()
        return create