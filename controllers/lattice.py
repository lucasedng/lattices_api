from flask import request
from flask_restplus import Resource, fields

from models.lattice import LatticeModel
from schemas.lattice import LatticeSchema
from server.instance import server

lattices_namespace = server.lattices_namespace

lattice_schema = LatticeSchema()
lattice_list_schema = LatticeSchema(many=True)

ITEM_NOT_FOUND = 'Lattice not found'

item = lattices_namespace.model('Lattice Model', {
    'name': fields.String('Example: "A2" '),
    'dimension': fields.Integer('Example: "2"'),
    'determinant': fields.Float('Example: "3.0"'),
    'minimal_norm': fields.Float('Example: "2.0"'),
    'kissing_number': fields.Integer('Example: "6"'),
    'gen_matrix': fields.String('Lattice generator matrix'),
    'gram_matrix': fields.String('Lattice gram matrix')
})


class Lattice(Resource):

    def get(self, id):
        lattice_data = LatticeModel.find_by_id(id)
        if lattice_data:
            return lattice_schema.dump(lattice_data), 200
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        lattice_data = LatticeModel.find_by_id(id)
        if lattice_data:
            lattice_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @lattices_namespace.expect(item)
    def put(self, id):
        lattice_data = LatticeModel.find_by_id(id)
        lattice_json = request.get_json()

        if lattice_data:
            lattice_data.name = lattice_json['name']
            lattice_data.dimension = lattice_json['dimension']
            lattice_data.determinant = lattice_json['determinant']
            lattice_data.minimal_norm = lattice_json['minimal_norm']
            lattice_data.kissing_number = lattice_json['kissing_number']
            lattice_data.gen_matrix = lattice_json['gen_matrix']
            lattice_data.gram_matrix = lattice_json['gram_matrix']
        else:
            lattice_data = lattice_schema.load(lattice_json)

        lattice_data.save_to_db()
        return lattice_schema.dump(lattice_data), 200

class LatticeList(Resource):

    @lattices_namespace.doc('Get all the Lattices')
    def get(self, ):
        return lattice_list_schema.dump(LatticeModel.find_all()), 200

    @lattices_namespace.expect(item)
    @lattices_namespace.doc('Create an Lattice')
    def post(self, ):
        lattice_json = request.get_json()
        print(lattice_json)
        lattice_data = lattice_schema.load(request.get_json())

        lattice_data.save_to_db()

        return lattice_schema.dump(lattice_data), 201
