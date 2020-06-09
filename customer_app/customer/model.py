from datetime import datetime

from customer_app.model import db


class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, index=True)
    dob = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @classmethod
    def get(cls, pk):
        return cls.query.get(int(pk))
