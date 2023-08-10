from flask import Flask, render_template
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
		return render_template('index.html')

	Api(app)

	return app