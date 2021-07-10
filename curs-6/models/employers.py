from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from models import DeclarativeBase, BaseModel


class Employer(DeclarativeBase, BaseModel):
    __tablename__ = 'employers'
    name = Column(VARCHAR(255), unique=True)
    employees = relationship('Employee',  back_populates='employer')


class Employee(DeclarativeBase, BaseModel):
    __tablename__ = 'employees'
    user_id = Column(INTEGER, ForeignKey('users.id'))
    user = relationship('User')
    employer_id = Column(INTEGER, ForeignKey(Employer.id))
    employer = relationship('Employer', back_populates='employees')
    wage = Column(INTEGER, nullable=False)
