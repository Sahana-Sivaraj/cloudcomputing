from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application_user import db
from run import app

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cloudacademy:pfm_2020@user-db:3306/user'
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()