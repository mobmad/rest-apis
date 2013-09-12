from flask import Flask
from flask import jsonify
from flask import request
from shows import Shows
from flask import render_template
import requests
from apiexception import ApiException

app = Flask(__name__)
shows = Shows()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/shows')
def get_shows():
	return jsonify(shows = shows.get())

@app.route('/shows', methods=['POST'])
def create_show():
	show = shows.add({
		'name': request.json['name'],
		'sid': request.json.get('sid', '')
	});
	return jsonify(show), 201

@app.route('/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
	show = shows.get(show_id)

	# TODO: Implement
	# Should get show rating from showratings API (remember to start it from 1-showratings-api) and merge the
	# rating into show['rating'] if the show was found in showratings-api
	#
	# Hint: requests has been imported for you and should be useful, see docs at:
	# http://docs.python-requests.org/en/latest/

	return jsonify(show)

@app.route('/shows/<int:show_id>', methods=['PUT'])
def update_show(show_id):
	show = shows.update(show_id, {
		'name': request.json['name'],
		'sid': request.json['sid']
	})
	return jsonify(show)

@app.route('/shows/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
	show = shows.delete(show_id)
	return jsonify(show)

@app.errorhandler(ApiException)
def handle_invalid_usage(error):
	response = jsonify({'error': error.message})
	response.status_code = error.status_code
	return response

if __name__ == '__main__':
	app.run(debug=True)