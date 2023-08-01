from flask import Blueprint
from flask_restful import Api, Resource

from .resources import Clasification, Players, Results, Schedule

bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp)

api.add_resource(Players, '/players')
api.add_resource(Results, '/results')
api.add_resource(Clasification, '/clasification')
api.add_resource(Schedule, '/schedule', '/calendar')