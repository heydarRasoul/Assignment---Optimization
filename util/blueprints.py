
# import routes
from routes.product_routes import product
from routes.category_routes import category
from routes.company_routes import company
from routes.warranty_routes import warranty


def register_blueprints(app):
    app.register_blueprint(company)
    app.register_blueprint(product)
    app.register_blueprint(category)
    app.register_blueprint(warranty)