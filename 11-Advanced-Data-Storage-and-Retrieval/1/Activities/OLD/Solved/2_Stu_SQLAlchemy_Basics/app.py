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

# print all rows
result = engine.execute("select * from songs")
for row in result:
    print(row)

# print titles only
result = engine.execute("select title from songs")
for row in result:
    print(row)


#--------- Use This Data -------------#

# DROP DATABASE IF EXISTS <this_is_the_random_db_jaws_creates_for_you>;
# CREATE DATABASE <this_is_the_random_db_jaws_creates_for_you>;

# USE <this_is_the_random_db_jaws_creates_for_you>;

# CREATE TABLE songs(
#   id INT NOT NULL AUTO_INCREMENT,
#   title VARCHAR(45) NULL,
#   artist VARCHAR(45) NULL,
#   genre VARCHAR(45) NULL,
#   PRIMARY KEY (id)
# );

# INSERT INTO songs (title, artist, genre)
# VALUES ("Human", "Krewella", "Dance");

# INSERT INTO songs (title, artist, genre)
# VALUES ("TRNDSTTR","Black Coast", "Dance");

# INSERT INTO songs (title, artist, genre)
# VALUES ("Whos Next", "The Who", "Classic Rock");

# INSERT INTO songs (title, artist, genre)
# VALUES ("Yellow Submarine", "The Beatles", "Classic Rock");
