from flask import Flask
from flask import jsonify
from shows import Shows
from apiexception import ApiException

app = Flask(__name__)
shows = Shows()

@app.route('/shows')
def get_shows():
	return jsonify(shows = shows.get())

@app.errorhandler(ApiException)
def handle_invalid_usage(error):
	response = jsonify({'error': error.message})
	response.status_code = error.status_code
	return response

if __name__ == '__main__':
	app.run(debug=True)