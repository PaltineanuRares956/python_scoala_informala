from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from models import DeclarativeBase, BaseModel
from models.employers import Employee


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'users'
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    employees = relationship(Employee, back_populates='user')

