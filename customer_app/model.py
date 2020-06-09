from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from customer_app import bcrypt

ma = Marshmallow()
db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), unique=True, index=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def is_password_correct(self, plain_password):
        return bcrypt.check_password_hash(self.password, plain_password)

    @classmethod
    def create(cls, username, password):
        user = cls(username=username)
        user.password = password
        db.session.add(user)
        return user
