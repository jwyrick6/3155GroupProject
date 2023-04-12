from models import db, User

class UserRepository:
  
    def create_user(self, name, password, email):
        user = User(name=name, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return user

user_repo_singleton = UserRepository()