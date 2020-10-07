import pymongo # make sure its in your pipenv
import dnspython
import sqlite3 # dont need to install

password = "?"
dbname = "?"

def create_mdb_connection(password, dbname):
  client = pymongo.MongoClient(
    "mongodb://nwdelafu:" + password + "@cluster0-shard-00-00.2v1mg.mongodb.net:27017,cluster0-shard-00-01.2v1mg.mongodb.net:27017,cluster0-shard-00-02.2v1mg.mongodb.net:27017/" + dbname + "?ssl=true&replicaSet=atlas-10tmua-shard-0&authSource=admin&retryWrites=true&w=majority"
  )
  return client

def create_sl_connection(extraction_db="rpg_db.sqlite3"):
  sl_conn = sqlite3.connect(extraction_db) # local sqlitedb
  return sl_conn

def execute_query(curs, query):
  return curs.execute(query) # executes query - specifically for SQLite


# SQLite Quiries
get_characters = "SELECT * FROM charactercreator_character"

# Documents - Remember we dont need to create a table, Mongo is not structured


if __name__ == "__main__":
  sl_conn = create_sl_connection()
  sl_curs = sl_conn.cursor()
  client = create_mdb_connection(password, dbname)
  characters = execute_query(sl_curs, get_characters) # will return a 
  print(type(characters))
  print(characters)