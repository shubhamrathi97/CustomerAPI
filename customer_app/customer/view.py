from flask import Blueprint

customer_api = Blueprint('customer', __name__)


@customer_api.route('/')
def hello_world():
    return 'Hello World!'
