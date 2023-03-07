from flask import Flask, jsonify, request
from .scrapper import get_players, get_clasification, get_results, get_schedule

def create_app():
	app = Flask(__name__)

	@app.get("/players")
	def players():
		return get_players()

	@app.get("/clasification")
	def clasification():
	  return get_clasification()

	@app.get("/results")
	def results():
		return get_results()

	@app.get("/schedule")
	def schedule():
		return get_schedule()

	return app
