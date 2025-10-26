from flask import Blueprint

import controllers

products = Blueprint('products', __name__)

@products.route('/product/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    return controllers.update_product_by_id(product_id)

# @app.route('/product', methods=['POST'])
