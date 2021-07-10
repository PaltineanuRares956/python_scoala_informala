from time import sleep
from handlers.database import DatabaseHandler, check_session
from models.users import User
from models.employers import Employer


@check_session
def load_users(session=None):
    return session.query(User).all()


@check_session
def load_employers(session=None):
    return session.query(Employer).all()


def load(callback_setter=None):
    session = DatabaseHandler.session
    users = load_users(session=session)
    employers = load_employers(session=session)

    sleep(1)  # simulate huge amount of data
    if callback_setter:
        callback_setter(users=users, employers=employers)
