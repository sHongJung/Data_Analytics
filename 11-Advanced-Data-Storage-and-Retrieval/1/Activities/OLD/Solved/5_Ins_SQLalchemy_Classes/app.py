import config as cfg
# iASEwmport create_engine so we can talk to our db
from sqlalchemy import create_engine
# import our sql client
import pymysql
pymysql.install_as_MySQLdb()
# create our connection
# import SQLAlchemy's declarative_base module, based upon which new classes are created
from sqlalchemy.ext.declarative import declarative_base
# base is akin to a template for creating classes
Base = declarative_base()
# modules necessary to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float
# import config so we can connect to JawsDB

# declare Dog as a class
class Dog(Base):
    __tablename__ = 'dog'
    
    # point out that we have a primary key here
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)

# create a new dog
dog = Dog(name='Fido', color='brown', age=4)
# Print the the surfer's name to the console
print(dog.name)

engine = create_engine(cfg.mysql['connection'])
# call create_all and pass in our connection
Base.metadata.create_all(engine)
# to persist dog objects into, and load from the database, we use a Session object

# WORKING WITH THE SESSION OBJECT
from sqlalchemy.orm import Session
# declare a session
session = Session(bind=engine)
# perform an UPDATE on the dog's age, check in workbench that the value is 5 not 4 now
dog.age += 1
# add dog to the session
session.add(dog)
# commit him to the database
session.commit()
