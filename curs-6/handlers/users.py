from .database import DatabaseHandler
from models.users import User
from .employees import fire

# delete the user
def delete(user):
    fire(user, user)
    session = DatabaseHandler.session
    users = session.query(User).filter(User.id == user.id)
    users.delete()
    session.commit()