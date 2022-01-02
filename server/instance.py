from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(
            self.blueprint,
            doc='/doc',
            default='Lattices Data',
            default_label='Everything about Lattices',
            title='A Catalogue of Lattices'
        )
        self.app.register_blueprint(self.blueprint)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.lattices_namespace = self.api.namespace(
            name='Lattices Data',
            description='Everything about Lattices',
            path='/'
        )

    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='localhost'
        )


server = Server()
