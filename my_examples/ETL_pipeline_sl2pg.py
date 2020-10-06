import pyscopg2
import sqlite3

pg_dbname = "?" # user and default username
pg_user = "?" # user and default username
pg_password = "?" # password through ElephantSQL - DO NOT SHARE
pg_host = "?" # copy from server on elephant SQL


def connect_to_pg(pg_dbname, pg_user, pg_password, pg_host), extraction_db='rpg_db.sqlite3':
  """ Connects to DB - return sl_conn & pg_conn """
  sl_conn = sqlite3.connect(extraction_db) # local SQLite db
  pg_conn = psycopg2.connect(pg_dbname=pg_dbname, pg_user=pg_user, pg_password=pg_password, pg_host=pg_host) # postgreSQL db
  return sl_conn, pg_conn

def execute_query(curs, query):
  return curs.execute(query).fetchall() #executes query depending on the cursor we have passed in

# Queries
create_pg_character_table = """
CREATE TABLE charactercreator_character (
  chracter_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""

# example for inserting a single character tuple to pg db
example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES""" + str(characters[0][1:]) + ";"

# for loop that runs through each character and stores in list
insert_characters = []
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(character[1:]) + ";"
  insert_characters.append(insert_character)

# check to see if we actually filled table
check_table_exist = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
  sl_conn, pg_conn = connect_to_pg(pg_dbname, pg_user, pg_password, pg_host)
  sl_curs = sl_conn.cursor()
  pg_curs = pg_conn.cursor()
  execute_query(pg_curs, create_pg_character_table) # creating table in pg db
  for insert_character in insert_characters: # iterating through the string we created for our quiries
    # print(insert_character) # uncomment (cmd+/) to give feedback if we want to make see if our individual query is correct
    execute_query(pg_curs, insert_character)

  pg_conn.commit() # only need to commit pg since no changes on SQLite
  execute_query(pg_curs, check_table_exists) # checks if it exist in PG DB

  
