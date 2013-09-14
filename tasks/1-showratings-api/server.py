from flask import Flask
from flask import jsonify
from flask import make_response
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'app99'
app.config['BASIC_AUTH_PASSWORD'] = 'pass99'

basic_auth = BasicAuth(app)

shows = [
	{
		"sid": 3001,
		"name": "Breaking Bad",
		"rating": "9.4"
	},
	{
		"sid": 3002,
		"name": "Dexter",
		"rating": "9.0"
	}
]

@app.route('/shows/<int:show_id>')
@basic_auth.required
def get_show(show_id):
	search = filter(lambda s: s['sid'] == show_id, shows)
	if len(search) == 0:
		return make_response(jsonify({'error': 'Show not found'}), 404)

	return jsonify(search[0])

if __name__ == '__main__':
	app.run(debug=True, port=5001)

# TODO: run server.py to start the server, and run curl and your browser against
# the API as instructed in the companion presentation