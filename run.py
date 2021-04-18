from app import create_app
from config import DevConfig

from app import db

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app(DevConfig())

if __name__ == '__main__':

    # DB Migrations
    # migrate = Migrate(app, db)
    # manager = Manager(app)
    # manager.add_command('db', MigrateCommand)

    app.run()
    # manager.run()