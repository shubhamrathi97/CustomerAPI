from customer_app.customer.model import CustomerModel
from customer_app.model import ma


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerModel
