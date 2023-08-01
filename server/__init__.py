from flask import Flask
from flask_restful import Api
from .api import bp

def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)

	@app.errorhandler(404)
	def not_found(e):
		return {
			'message': 'Not found'
		}, 404

	@app.get('/')
	def index():
		return {
			'message': 'Go to /api endpoint',
			'endpoints': ['players', 'results', 'clasification', 'schedule']
		}

	Api(app)

	return app