#!/usr/bin/python3
"""Flask app initialization"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Returns a string at the /cities_by_states route"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)