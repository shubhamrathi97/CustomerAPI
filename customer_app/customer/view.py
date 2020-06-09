from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from customer_app.helper import verified_request
from customer_app.model import db
from .model import CustomerModel
from .schema import CustomerSchema

customer_api = Blueprint('customer', __name__, url_prefix='/customers')


@customer_api.route('/', methods=['GET'])
@verified_request
def get_customers():
    customer_schema = CustomerSchema(many=True)
    customers_query = CustomerModel.query.order_by(desc(CustomerModel.dob))
    n = request.args.get('n')
    if n and int(n):
        customers_query = customers_query.limit(n)
    customers_data = customers_query.all()
    return jsonify({'customers': customer_schema.dump(customers_data), 'result': 'success'})


@customer_api.route('/', methods=['POST'])
@verified_request
def add_customer():
    req_data = request.get_json()
    valid_req_data = CustomerSchema().load(req_data)
    customer_obj = CustomerModel(**valid_req_data)
    db.session.add(customer_obj)
    db.session.commit()
    customer_json = CustomerSchema().dump(customer_obj)
    return jsonify({'customer': customer_json, 'result': 'success'}), 201


@customer_api.route('/<int:pk>/', methods=['GET'])
@verified_request
def get_customer(pk: int):
    customer = CustomerModel.get(pk)
    customer_schema = CustomerSchema()
    customer_json = customer_schema.dump(customer)
    return jsonify({'customer': customer_json, 'result': 'success'})


@customer_api.route('/<int:pk>/', methods=['PUT'])
@verified_request
def update_customer(pk: int):
    customer = CustomerModel.get(pk)
    customer_schema = CustomerSchema()
    req_data = request.get_json()
    valid_req_data = customer_schema.load(req_data, partial=True)
    for field in valid_req_data:
        if hasattr(customer, field):
            setattr(customer, field, valid_req_data[field])
    db.session.commit()
    customer_json = customer_schema.dump(customer)
    return jsonify({'customer': customer_json, 'result': 'success'})


@customer_api.route('/<int:pk>/', methods=['DELETE'])
@verified_request
def delete_customer(pk: int):
    customer = CustomerModel.get(pk)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'result': 'success'})
