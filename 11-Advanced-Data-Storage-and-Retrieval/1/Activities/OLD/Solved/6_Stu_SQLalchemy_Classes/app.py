import config as cfg
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float

class Surfer(Base):
    __tablename__ = 'surfer'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hometown = Column(String(255))
    age = Column(Integer)
    rating = Column(Float)

from sqlalchemy import create_engine
engine = create_engine(cfg.mysql['connection'])
Base.metadata.create_all(engine)

jack = Surfer(name='Jack Johnson', hometown='Oahu', age=42, rating='9.3')
print(jack.name)

from sqlalchemy.orm import Session

# add a surfer
session = Session(bind=engine)
session.add(jack)
# you can update the session with dot notation
jack.age += 1
session.commit()

# find a surfer
session1 = Session(bind=engine)
surfer = session1.query(Surfer).filter_by(name='Jack Johnson').first()
print(surfer.name)

# add multiple surfers into session
session2 = Session(bind=engine)
session2.add_all([
    Surfer(name='Kelly Slater', hometown='Oahu', age=42, rating='9.3'),
    Surfer(name='Mike Stewart', hometown='Sunset Beach', age=52, rating='9.1'),
    Surfer(name='Jordy Stewart', hometown='Malibu', age=48, rating='9.8')
])
session2.commit()

# delete a surfer by id
session3 = Session(bind=engine)
session3.query(Surfer).filter(Surfer.id == 1).\
     delete()
session3.commit()

# delete all surfers that mach the query 
session4 = Session(bind=engine)
session4.query(Surfer).filter(Surfer.name == "Jack Johnson").\
    delete(synchronize_session='evaluate')
session4.commit()
