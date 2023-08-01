from flask_restful import Resource, fields
from .scrapper import get_clasification, get_players, get_results, get_schedule

class Players(Resource):
	def get(self):
		return get_players()

class Results(Resource):
	def get(self):
		return get_results()

class Clasification(Resource):
	def get(self):
		return get_clasification()
 
class Schedule(Resource):
	def get(self):
		return get_schedule()
