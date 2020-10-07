"""An example of how to import the characters table into MongoDB from SQLite"""

import pymongo  # make sure its in your pipenv
import sqlite3  # dont need to install


password = "?"
dbname = "?"

def create_mdb_connection(password, dbname):
    # using string formatting to add in my password and dbname
    client = pymongo.MongoClient(
        "mongodb://nwdelafu:{}@cluster0-shard-00-00.2v1mg.mongodb.net:27017,cluster0-shard-00-01.2v1mg.mongodb.net:27017,cluster0-shard-00-02.2v1mg.mongodb.net:27017/{}?ssl=true&replicaSet=atlas-10tmua-shard-0&authSource=admin&retryWrites=true&w=majority"
        .format(password, dbname))
    return client

def create_sl_connection(extraction_db="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)  # local sqlitedb
    return sl_conn

def execute_query(curs, query):
    return curs.execute(
        query).fetchall()  # executes query - specifically for SQLite

# You can make this more robut by using something like the show_sl_schema function we made
# How can you make this with insert_many?
def character_doc_creation(db, character_table):
    for character in character_table:
        # character - (id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]
        }
        db.insert_one(character_doc)

def show_sl_schema(table):
    schema = "PRAGMA table_info(" + table + ");"

def show_all(db):
    all_docs = list(db.find())
    return all_docs


# SQLite Quiries
get_characters = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(password, dbname)
    db = client.test
    characters = execute_query(sl_curs, get_characters)  # will return a list
    character_doc_creation(db.test, characters)
    print(show_all(db.test))
