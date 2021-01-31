# application1/__init__.py
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

import config
from flask import Flask, jsonify

from application.models import db, Product
from application.sat_api import product_api_blueprint
from application import hub


def create():
    print('started')
    hub.execute_adding_data()


app = Flask(__name__)
environment_configuration = config.ProductionConfig
app.config.from_object(environment_configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = config.ProductionConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
migrate: Migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all()
app.register_blueprint(product_api_blueprint)

create()
