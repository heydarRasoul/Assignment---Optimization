


def get_companies():
    company_query = db.session.query(Companies).all()
    
    if not company_query:
        return jsonify({"message": "no companies found"}), 404
    
    else:
      return jsonify({"message": "companies found", "results": companies_schema.dump(company_query)}), 200
