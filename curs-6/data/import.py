import json
from models.users import User
from models.employers import Employer
from handlers.database import DatabaseHandler

if __name__ == "__main__":
    session = DatabaseHandler.session

    db_users = session.query(User).all()
    if len(db_users) == 0:
        with open('users.json', 'r') as users_file:
            users_to_import = json.load(users_file) or []

        for user_data in users_to_import:
            session.add(
                User(
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    email=user_data["email"],
                )
            )

    db_employers = session.query(Employer).all()
    if len(db_employers) == 0:
        with open('employers.json', 'r') as employers_file:
            employers_to_import = json.load(employers_file) or []

        for employer_data in employers_to_import:
            session.add(
                Employer(
                    name=employer_data["name"],
                )
            )

    session.commit()
