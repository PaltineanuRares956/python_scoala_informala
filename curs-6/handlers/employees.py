from .database import DatabaseHandler
from models.employers import Employee


def hire(user, employer):
    session = DatabaseHandler.session
    session.add(Employee(
        user=user,
        employer=employer,
        wage=10,
    ))
    session.commit()


def fire(user, employer):
    session = DatabaseHandler.session
    employee = session.query(Employee).filter(Employee.user == user, Employee.employer == employer)
    employee.delete()
    session.commit()

