# for creating tables and column structure for our database

from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# Create Table in sqlite -- by creating/defining a class


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)  # when a newtodo is created by default it is false
    





