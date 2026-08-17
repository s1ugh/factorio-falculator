import os
import psycopg2
import json
from dotenv import load_dotenv

ITEMS_FACTORIO_JSON = 'data/items_factorio.json'

load_dotenv()

class FactorioDatabase:

    def __init__(self):
        self.db_user = os.getenv('DB_USER')
        self.db_name = os.getenv('DB_NAME')
        self.db_password = os.getenv('DB_PASSWORD')
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname = self.db_name,
                user = self.db_user,
                password = self.db_password,
                host = "127.0.0.1"
              )
            print('The connection to the database was successful')
        except psycopg2.Error as ex_:
            print('[INFO] Error while working with PostgreSQL', ex_)

    def create_tables(self, name_table, columns_schema):
        """
        name_table: str
        columns_schema: str
        """

        if not self.connection:
            print('No connection to database')
            return None

        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {name_table} (
                            {columns_schema}
                        );
                    """)
                    print(f'Table {name_table} created')
                    return True
        except psycopg2.Error as e:
            print(f'Error creating table {e}')
            return False


    def insert_data(self, table_name, data_list):

        columns = ", ".join(data_list[0].keys())
        placeholder = ', '.join(['%s'] * len(data_list[0]))

        query = f"""
            INSERT INTO {table_name}({columns})
            VALUES ({placeholder})
            ON CONFLICT DO NOTHING;
        """
        values = [tuple(d.values()) for d in data_list]

        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.executemany(query, values)


    def __del__(self):
        if self.connection:
            self.connection.close()
            print('Connection to database closed')

if __name__ == '__main__':
    db = FactorioDatabase()
    db.connect()
    db.create_tables('items', 'name VARCHAR PRIMARY KEY, stack_size INTEGER')

    with open(ITEMS_FACTORIO_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    prepared_items = []
    for item_name, item_details in data.items():
        prepared_items.append({
            'name': item_name,
            'stack_size': item_details.get('stack_size')
        })

    db.insert_data('items', prepared_items)

