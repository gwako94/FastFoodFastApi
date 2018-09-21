import psycopg2
import os


class Database():

    def __init__(self):
        self.host = os.getenv('host')
        self.dbname = os.getenv('dbname')
        self.user = os.getenv('user')
        self.password = os.getenv('password')
