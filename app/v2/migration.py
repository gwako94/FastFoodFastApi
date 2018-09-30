"""Implements database"""
import psycopg2
from psycopg2.extras import RealDictCursor
import os


class Database(object):

    #constructor initialize environment
    def __init__(self):
        self.host = os.getenv('HOST')
        self.name = os.getenv('DEV_DB')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')

        try:
            self.conn = psycopg2.connect(host=self.host, dbname=self.name, user=self.user, password=self.password)
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        except:
            print("Unable to connect to the database")


    
    def create_tables(self):
        """ Method to create tables """

        users = '''CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(70) UNIQUE NOT NULL,
                    password VARCHAR(250) NOT NULL,
                    admin bool,
                    created_at TIMESTAMP
        );'''

        menu =  '''CREATE TABLE IF NOT EXISTS menu(
                    menu_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(50) NOT NULL,
                    image_url VARCHAR(270) NOT NULL,
                    price numeric NOT NULL,
                    created_at TIMESTAMP
                    
        );'''

        orders = '''CREATE TABLE IF NOT EXISTS orders(
                    order_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    cart VARCHAR(200) NOT NULL,
                    total numeric NOT NULL,
                    status VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP
                    
        );'''
        queries = [users, menu, orders]

        for query in queries:
            self.cur.execute(query)
            self.conn.commit()
        print("All tables created successfully!")
        self.cur.close()

    def drop_tables(self):
        query = "DROP TABLE users, menu, orders;"
        self.cur.execute(query)
        self.conn.commit()
        print("All tables dropped successfully!")
        self.cur.close()