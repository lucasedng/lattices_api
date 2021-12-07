from db import db
from typing import List


class LatticeModel(db.Model):
    __tablename__ = 'lattices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    dimension = db.Column(db.Integer, nullable=False)
    determinant = db.Column(db.Float, nullable=False)
    minimal_norm = db.Column(db.Float, nullable=False)
    kissing_number = db.Column(db.Integer, nullable=False)
    gen_matrix = db.Column(db.String, nullable=False)
    gram_matrix = db.Column(db.String, nullable=False)

    def __init__(self, name, dimension, determinant, minimal_norm, kissing_number, gen_matrix, gram_matrix):
        self.name = name
        self.dimension = dimension
        self.determinant = determinant
        self.minimal_norm = minimal_norm
        self.kissing_number = kissing_number
        self.gen_matrix = gen_matrix
        self.gram_matrix = gram_matrix

    def __repr__(self, ):
        representation = \
            f'LatticeModel(name = {self.name}, dimension = {self.dimension}, '\
            f'determinant = {self.determinant}, minimal_norm = {self.minimal_norm}, '\
            f'kissing_number= {self.kissing_number}, gen_matrix = {self.gen_matrix}, gram_matrix = {self.gram_matrix})'

        return representation

    def json(self, ):
        return {
            'name': self.name,
            'dimension': self.dimension,
            'determinant': self.determinant,
            'minimal_norm': self.minimal_norm,
            'kissing_number': self.kissing_number,
            'gen_matrix': self.gen_matrix,
            'gram_matrix': self.gram_matrix
        }

    @classmethod
    def find_by_name(cls, _name) -> "LatticeModel":
        return cls.query.filter_by(name=_name).first()

    @classmethod
    def find_by_id(cls, _id) -> "LatticeModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["LatticeModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
