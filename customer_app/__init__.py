import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_filename):
    app = Flask(__name__)
    # Loading Config from File
    app.config.from_pyfile(os.path.join(os.path.curdir, config_filename))
    # Initializing bcrypt
    bcrypt.init_app(app)
    # Initializing JWT
    jwt.init_app(app)
    # Registering Marshmallow
    from customer_app.model import ma
    ma.init_app(app)

    # Registering SQLAlchemy
    from customer_app.model import db
    db.init_app(app)

    # Registering API
    from customer_app.customer.view import customer_api
    app.register_blueprint(customer_api)

    from customer_app.view import api_route
    app.register_blueprint(api_route)
    return app
