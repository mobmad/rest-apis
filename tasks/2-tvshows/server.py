from flask import Flask
from flask import jsonify
from shows import Shows
from apiexception import ApiException

app = Flask(__name__)
shows = Shows()

@app.route('/shows')
def get_shows():
	return jsonify(shows = shows.get())

# TODO: create new methods for getting a single show, as well as
# creating, updating and deleting a show. You should use the
# Shows class, already used by get_shows(), which simulates a 
# store for tv shows. In a real project, you would probably have 
# the data stored in a database of some kind, but here we just
# store them in memory for simplicity. Note: when you make changes
# to files, the server will restart and the in-memory shows will be
# lost.
#
# As you implement the metods, you should verify that they work by 
# using curl. See 1-showratings-api-solution for curl examples.
#
# Remember to start 2-tvshows/server.py. The tvshows tasks run on 
# a different port (5000) than the showratings-api (port 5001). 
# The reason will be clear in task 5.


@app.errorhandler(ApiException)
def handle_invalid_usage(error):
	response = jsonify({'error': error.message})
	response.status_code = error.status_code
	return response

if __name__ == '__main__':
	app.run(debug=True)