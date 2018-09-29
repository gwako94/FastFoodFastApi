import os
from flask_script import Manager

from app.v2.migration import Database
from app.app import create_app
env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

db = Database()
manager = Manager(app)

@manager.command
def create_tables():
    db.create_tables()

if __name__ == '__main__':
    manager.run()