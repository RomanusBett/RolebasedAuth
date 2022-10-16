from datetime import datetime
import psycopg2

# local imports
from flask import current_app


class DataStore:
    """ database connection model """

    def __init__(self):
        self.db_host = current_app.config['DB_HOST']
        self.db_username = current_app.config['DB_USERNAME']
        self.db_password = current_app.config['DB_PASSWORD']
        self.db_name = current_app.config['DB_NAME']
        self.conn = psycopg2.connect(
            host=self.db_host,
            user=self.db_username,
            password=self.db_password,
            database=self.db_name,
        )
        self.cur = self.conn.cursor()

    def create_table(self, schema):
        """ method to create a table """
        self.cur.execute(schema)
        self.save()

    def drop_table(self, name):
        """ method to drop a table """
        self.cur.execute("DROP TABLE IF EXISTS " + name)
        self.save()

    def save(self):
        """ method to save the changes made """
        self.conn.commit()

    def close(self):
        self.cur.close()


class Meals(DataStore):

    def __init__(self, name=None, price=None,  subsidy=None):
        super().__init__()
        self.name = name
        self.price = price
        self.subsidy = subsidy
        self.date = datetime.now().replace(second=0, microsecond=0)
