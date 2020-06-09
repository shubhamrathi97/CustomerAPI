from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from customer_app import create_app
from customer_app.model import db
import os

app = create_app(os.getenv('config_filename','config.py'))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#
# @manager.command
# def runworker():
#     redis_connection = app.redis_conn
#     with Connection(redis_connection):
#         worker = Worker(app.config['RQ_QUEUES'])
#         worker.work()


if __name__ == '__main__':
    manager.run()
