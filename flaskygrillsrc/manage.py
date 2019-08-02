
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models


config_name = os.environ.get("FLASK_ENV")
app = create_app(config_name)
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)   # commands include : 
                                            # python manager.py db 'init'   -> creates migrations folder(has 'versions' folder with all migration scripts)
                                            # python manager.py db 'migrate'->-like makemigrations,       -> makes  the actual migrations
                                            # python manager.py db 'upgrade'->-like migrate               -> applies migrations to the database


if __name__ == "__main__":
    manager.run()