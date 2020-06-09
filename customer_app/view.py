from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

from customer_app.model import UserModel, db

api_route = Blueprint('main', __name__)


@api_route.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'error': 'Request accepts json data only', 'result': 'error'})

    req_data = request.get_json()
    if not (req_data.get('username') and req_data.get('password')):
        return jsonify({'error': 'Username/ Password missing', 'result': 'error'})

    user = UserModel.query.filter(UserModel.username == req_data.get('username')).first()
    if user.is_password_correct(req_data.get('password')):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)
        return jsonify({'data': {'access_token': access_token, 'refresh_token': refresh_token}, 'result': 'success'})
    return jsonify({'result': 'error', 'error': 'Username/Password Incorrect'})


@api_route.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({'error': 'Request accepts json data only', 'result': 'error'})
    req_data = request.get_json()
    if not (req_data.get('username') and req_data.get('password')):
        return jsonify({'error': 'Username/ Password missing', 'result': 'error'})
    user = UserModel.create(req_data.get('username'), req_data.get('password'))
    db.session.commit()
    return jsonify({'result': 'success', 'data': {'username': user.username}}), 201


# Standard refresh endpoint. A blacklisted refresh token
# will not be able to access this endpoint
@api_route.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200
