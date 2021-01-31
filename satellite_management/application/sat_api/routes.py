# application1/product_api/routes.py
from flask import Blueprint

from application import db
from application.models import Product
from flask import jsonify, request

from application.sat_api import product_api_blueprint


@product_api_blueprint.route('/api/sat/create', methods=['POST'])
def post():
    name = request.form['name']
    print(name)
    location = request.form['location']
    print(location)
    healthy = request.form['healthy']
    print(healthy)
    item = Product()
    item.name = name
    item.healthy = healthy
    item.location = location
    db.session.add(item)
    db.session.commit()
    response = jsonify({'message': 'Satllite added', 'satllite': item.to_json()})
    return response


@product_api_blueprint.route('/api/sat/<id>', methods=['DELETE'])
def delete_sa(id):
    task = Product.query.get(id)
    print(task)
    db.session.delete(task)
    db.session.commit()
    response = jsonify({'message': 'Deleted'}), 200
    return response


@product_api_blueprint.route('/api/sat/healthy/<id>', methods=['PUT'])
def update_satehealthy(id):
    healthy = request.form['healthy']
    print(healthy)
    task = Product.query.get(id)
    task.healthy = healthy
    db.session.commit()
    response = jsonify({'message': 'Updated Status'}), 200
    return response

@product_api_blueprint.route('/api/sat/location/<id>', methods=['PUT'])
def update_satelocation(id):
    location = request.form['location']
    print(location)
    task = Product.query.get(id)
    task.location = location
    db.session.commit()
    response = jsonify({'message': 'Updated Location'}), 200
    return response

@product_api_blueprint.route('/api/sat/<id>', methods=['GET'])
def get_satlocation(id):
    item = Product.query.filter_by(id=id).first()
    print(item.to_json())
    if item is not None:
        response = jsonify({'result': item.to_json()})
    else:
        response = jsonify({'message': 'Cannot find sat'}), 404
    return response

@product_api_blueprint.route('/api/sats', methods=['GET'])
def get_users():
    data = []
    for row in Product.query.all():
        data.append(row.to_json())
    print(data)
    response = jsonify({'results': data})
    return response
