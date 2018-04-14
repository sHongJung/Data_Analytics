import config as cfg
import pymysql
pymysql.install_as_MySQLdb()

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine(cfg.mysql['connection'])

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

EA = Base.classes.europe
NA = Base.classes.northamerica

#------------We Don't Have To Define These Clases Because We Are Using automap_base------------#
# class Europe(Base):
#     __tablename__ = 'europe'
#     id = Column(Integer, primary_key=True)
#     record_id = Column(Integer)
#     continent = Column(String(2))
#     status = Column(String(10))
#     sporder = Column(String(15))
#     family = Column(String(16))
#     genus = Column(String(16))
#     species = Column(String(16))
#     log_mass_g = Column(Integer)
#     comb_mass_g = Column(Integer)
#     reference = Column(String(19))


# class NorthAmerica(Base):
#     __tablename__ = 'northamerica'
#     id = Column(Integer, primary_key=True)
#     record_id = Column(Integer)
#     continent = Column(String(2))
#     status = Column(String(10))
#     sporder = Column(String(15))
#     family = Column(String(16))
#     genus = Column(String(16))
#     species = Column(String(16))
#     log_mass_g = Column(Integer)
#     comb_mass_g = Column(Integer)
#     reference = Column(String(19))

session = Session(engine)

# select all animals with the following attributes
results = [EA.family, EA.genus, EA.species, NA.family, NA.genus, NA.species]
# query on that select and filter by sporder, return the animals that match
same_sporder = session.query(*results).filter(EA.sporder == NA.sporder).all()

for record in same_sporder:
    (ea_fam, ea_gen, ea_spec, na_fam, na_gen, na_spec) = record
    print(
        f"The European animal '{ea_fam} {ea_gen} {ea_spec}'"
        f"belongs to the same sporder as the North American aniimal '{na_fam} {na_gen} {na_spec}'.")