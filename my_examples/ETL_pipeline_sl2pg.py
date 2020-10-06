import psycopg2
import sqlite3

pg_dbname = "?"
pg_user = "?"
pg_password = "?"
pg_host = "?"


def connect_to_pg(pg_dbname, pg_user, pg_password, pg_host, extraction_db='rpg_db.sqlite3'):
  """ Connects to DB - return sl_conn & pg_conn """
  sl_conn = sqlite3.connect(extraction_db) # local SQLite db
  pg_conn = psycopg2.connect(dbname=pg_dbname, user=pg_user, password=pg_password, host=pg_host) # postgreSQL db
  return sl_conn, pg_conn

def execute_query(curs, query):
  return curs.execute(query)  #executes query depending on the cursor we have passed in


# Queries
# creating characters list
get_characters = "SELECT * FROM charactercreator_character"

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
# example_insert = """
# INSERT INTO charactercreator_character
# (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
# VALUES""" + str(characters[0][1:]) + ";"

# check to see if we actually filled table
check_table_exist = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
  sl_conn, pg_conn = connect_to_pg(pg_dbname, pg_user, pg_password, pg_host)
  sl_curs = sl_conn.cursor()
  pg_curs = pg_conn.cursor()
  print(sl_curs)
  characters = execute_query(sl_curs, get_characters)
  execute_query(pg_curs, create_pg_character_table) # creating table in pg db
  
  for character in characters:
    insert_character = """
      INSERT INTO charactercreator_character
      (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
      VALUES""" + str(character[1:]) + ";"
    execute_query(pg_curs, insert_character)

  pg_conn.commit() # only need to commit pg since no changes on SQLite
  execute_query(pg_curs, check_table_exist) # checks if it exist in PG DB
