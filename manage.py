import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from customer_app import create_app
from customer_app.model import db

app = create_app(os.getenv('config_filename', 'config.py'))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
