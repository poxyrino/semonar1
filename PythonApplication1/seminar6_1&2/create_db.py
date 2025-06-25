import os
import sqlite3

db_name = 'dhcp_snooping.db'
schema_file = 'dhcp_snooping_schema.sql'

def create_database(db_name, schema_file):
    if not os.path.exists(db_name):
        print("Создаю базу данных...")

        connection = sqlite3.connect(db_name)
        with open(schema_file) as f:
            schema = f.read()
        connection.executescript(schema)
        connection.close()
    else:
        print("База данных существует")

create_database(db_name, schema_file)

