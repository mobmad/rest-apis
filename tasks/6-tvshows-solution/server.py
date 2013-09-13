from flask import Flask
from flask import jsonify
from flask import request
from shows import Shows
from flask import render_template
from flask import url_for
import requests
from apiexception import ApiException

app = Flask(__name__)
shows = Shows()

SHOWRATINGS_HOST='http://localhost:5001'
SHOWRATINGS_USER='app99'
SHOWRATINGS_PASS='pass99'

def add_links(show):
	decorated = show.copy()
	decorated['_links'] = {
		'self': url_for("get_show", show_id=show['id'], _external=True),
		'edit': url_for("update_show", show_id=show['id'], _external=True),
		'delete': url_for("delete_show", show_id=show['id'], _external=True)
	}
	return decorated

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/shows')
def get_shows():
	shows_with_links = map(add_links, shows.get())
	return jsonify(shows = shows_with_links, _links = {"create": url_for("get_shows", _external=True)})

@app.route('/shows', methods=['POST'])
def create_show():
	show = shows.add({
		'name': request.json['name'],
		'sid': request.json.get('sid', '')
	});
	return jsonify(show), 201

@app.route('/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
	show = add_links(shows.get(show_id))
	r = requests.get('{0}/shows/{1}'.format(SHOWRATINGS_HOST, show['sid']), auth=(SHOWRATINGS_USER, SHOWRATINGS_PASS))

	if r.status_code == 200:
		show['rating'] = r.json()['rating']

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