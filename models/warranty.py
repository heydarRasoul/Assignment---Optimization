import uuid 
from sqlalchemy.dialects.postgresql import UUID 
import marshmallow as ma

from db import db


class Warranties(db.Model):
    __tablename__ = 'Warranties'

    warranty_id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    product_id = db.Column(UUID(as_uuid=True), db.Foreign_key("Product.product_id"), nullable=False )
    warranty_month = db.Column(db.String(), nullable= False)


    products = db.relationship('Products' , foreign_keys=['Warranties.product_id'], back_populates='warranties')

    def __init__(self, product_id, warranty_months):
        self.product_id = product_id
        self.warranty_months = warranty_months


class WarrantiesSchema(ma.Schema):
    class Meta:
        fields = ['warranty_id', 'product_id',' warranty_months']

    product = ma.fields.Nested("ProductsSchema", exclude=['categories'])


warranty_schema = WarrantiesSchema()
warranties_schema = WarrantiesSchema(many=True)