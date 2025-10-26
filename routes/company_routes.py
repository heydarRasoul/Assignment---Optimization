from flask import Blueprint
import controllers

companies = Blueprint('companies', __name__)

@companies.route('/companies', methods=['GET'])
def get_companies():
  return controllers.get_companies()