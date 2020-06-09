from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)

    # Registering Marshmallow
    from customer_app.model import ma
    ma.init_app(app)

    # Registering SQLAlchemy
    from customer_app.model import db
    db.init_app(app)


    # Loading Config from File
    app.config.from_pyfile(config_filename)

    # Registering API
    from customer_app.customer.view import customer_api
    app.register_blueprint(customer_api)
    return app
