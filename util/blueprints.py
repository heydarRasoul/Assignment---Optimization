
import routes
# from routes import products, categories, companies, warranties


def register_blueprints(app):
    app.register_blueprint(routes.companies)
    app.register_blueprint(routes.products)
    app.register_blueprint(routes.categories)
    app.register_blueprint(routes.warranties)