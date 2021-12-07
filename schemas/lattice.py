from ma import ma
from models.lattice import LatticeModel

class LatticeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LatticeModel
        load_instance = True