import config as cfg
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float

# create your shark class
class Sharks(Base):
    __tablename__ = 'sharks'
    id = Column(Integer, primary_key=True)
    case_number = Column(String(255))
    date = Column(String(255))
    year = Column(Integer)
    type = Column(String(255))
    country = Column(String(255))
    area = Column(String(255))
    location= Column(String(255))
    activity = Column(String(255))
    name = Column(String(255))
    sex = Column(String(255))
    age = Column(Integer)
    injury = Column(String(255))
    fatal_y_n = Column(String(1))
    time = Column(String(255))
    species = Column(String(255))
    investigator_or_source = Column(String(255))
    pdf = Column(String(255))
    original_order = Column(Integer)

from sqlalchemy import create_engine
engine = create_engine(cfg.mysql['connection'])
Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# print all locations of shark attacks
attacks = session.query(Sharks) 
for attack in attacks:
    print(attack.location)

# find the number of provoked attacks
provoked = session.query(Sharks).filter_by(type='provoked').count()
print(provoked)

# find the number of attacks in USA
usa = session.query(Sharks).filter_by(country='USA').count()
print(usa)

# find the number of attacks in 2017
year_2017 = session.query(Sharks).filter_by(year=2017).count()
print(year_2017)

# find the number of attacks while surfing
surfing = session.query(Sharks).filter_by(activity='surfing').count()
print(surfing)

# find the number of fatal attacks
fatal = session.query(Sharks).filter_by(fatal_y_n='Y').count()
print(fatal)

# find the number of fatal attacks while surfing
fatal_surfing = session.query(Sharks).filter_by(fatal_y_n='Y').filter(Sharks.area == "Eastern Cape Province").count()
print(fatal_surfing)

# find the number of fatal attacks in 2017 in Australia
fatal_surfing = session.query(Sharks).filter_by(fatal_y_n='Y').filter(Sharks.country == "MOZAMBIQUE").filter(Sharks.activity == 'Spearfishing').count()
print(fatal_surfing)

# Bonus:
# find the location with the most attacks in 2017