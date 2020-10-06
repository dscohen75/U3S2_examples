import psycopg2

dbname = "?" # user and default username
user = "?" # user and default username
password = "?" # password through ElephantSQL - DO NOT SHARE
host = "?" # copy from server on elephant SQL

def connect_to_db(db_name, user, password, host):
  return psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

def execute_query(cursor, query):
  cursor.execute(query)
  return cursor.fetchall()


# QUERIES
create_table_statement = """
  CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""

insert_statement = """
  INSERT INTO test_table (name, data) VALUES
    (
      'A row name',
      null
    ),
    (
      'Another row, with JSON',
      '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
    );
"""

table_check = "SELECT * FROM test_table"


if __name__ == "__main__":
  conn = connect_to_db(dbname, user, password, host)
  curs = conn.cursor()
  # stretch goald - how can you make it so you don't get an error from the below function when running this file twice?
  execute_query(curs, create_table_statement) # this will give an error if we run twice, how can we fix? (try and execpt? Special SQL command?)
  execute_query(curs, execute_query)
  conn.commit()
  print(execute_query(query)) # checks to make sure we have the table by printing contents
                    