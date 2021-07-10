from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def check_session(function):
    """Decorator for checking existence of """
    def wrapper(*args, session=None, **kwargs):
        if not session:
            raise BaseException('Database session not available.')

        return function(*args, session=session, **kwargs)

    return wrapper


class DatabaseHandler:
    """Handler for creating a database session."""
    engine = create_engine("mysql+mysqldb://root:root@localhost:3306/python_db")
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
