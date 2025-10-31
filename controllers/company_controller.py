
from flask import request, jsonify

from db import db
from models.company import Companies, companies_schema, company_schema
from util.reflection import populate_object

def add_company():
    post_data = request.form if request.form else request.get_json()

    new_company = Companies.new_company_obj()
    populate_object(new_company, post_data)

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "company created", "result": company_schema.dump(new_company)}), 201


def get_companies():
    company_query = db.session.query(Companies).all()
    
    if not company_query:
        return jsonify({"message": "no companies found"}), 404
    
    else:
      return jsonify({"message": "companies found", "results": companies_schema.dump(company_query)}), 200


def get_company_by_id(company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id ).first()

    if not company_query:
        return jsonify({"message": "no company with provided id founded."})
    else:
        return jsonify({"message": "company found", "result": company_schema.dump(company_query)}),200
    

def update_company_by_id(company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    post_data = request.form if request.form else request.get_json()

    if company_query:
        populate_object(company_query, post_data)

        db.session.commit()
   
        return jsonify({"message": "company found", "results": company_schema.dump(company_query)}), 200
    
    return jsonify({"message": "unable to update record"}), 400


def delete_company_by_id(company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    if company_query:
        db.session.delete(company_query)
        db.session.commit()

        return jsonify({"message":"company deleted"}),200
    
    return jsonify({"message":"unable to delete company"}), 400
        
    