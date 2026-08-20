import os
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.exc import SQLAlchemyError
from models import Base, ItemModel

ITEMS_FACTORIO_JSON = 'data/items_factorio.json'

load_dotenv()

class FactorioDatabase:

    def __init__(self):
        self.db_user = os.getenv('DB_USER')
        self.db_name = os.getenv('DB_NAME')
        self.db_password = os.getenv('DB_PASSWORD')
        self.engine = create_engine(f'postgresql+psycopg2://{self.db_user}:{self.db_password}@127.0.0.1:5432/{self.db_name}')
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):

        try:
            Base.metadata.create_all(self.engine)

        except SQLAlchemyError as e:
            print(f'Error creating table {e}')
            return False

    def save_objects(self, objects_list):
        with self.Session() as session:

            try:
                session.add_all(objects_list)
                session.commit()
                print('Objects were saved')
            except SQLAlchemyError as e:
                session.rollback()
                print(f'Error save_objects: {e}')



if __name__ == '__main__':
    db = FactorioDatabase()
    db.create_tables()

    with open(ITEMS_FACTORIO_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items_to_save = []
    for item_name, item_details in data.items():
        db_item = ItemModel(
            name = item_name,
            stack_size = item_details.get('stack_size')
        )
        items_to_save.append(db_item)
    db.save_objects(items_to_save)
