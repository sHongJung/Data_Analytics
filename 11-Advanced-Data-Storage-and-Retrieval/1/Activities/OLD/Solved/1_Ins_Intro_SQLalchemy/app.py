# import config as cfg, so we can access our connection string from our config.py. 
# you should have set up jawsdb in heroku before this.
import config as cfg

# Import create engine so we can connect to our db
from sqlalchemy import create_engine

# import your sql client, pymsyql is a replacement for MySQLdb, but you could use either
import pymysql
pymysql.install_as_MySQLdb()

# create your engine and pass in your connection, from your config.py
engine = create_engine(cfg.mysql['connection'])

# demos that you can connect to your remote db and print out tables/attributes. 
# you can change this up depending on the dataset you use.
tables = engine.execute("SELECT * FROM Pigeon")
for index, table in enumerate(tables):
    table_name = table[1]
    print(f"The breeder for index {index} is called '{table_name}'.")