#!/usr/bin/python3
"""
Script to start a Flask web application
web app must be listening on 0.0.0.0:5000
/: will display "Hello HBNB!"
/hbnb: will display "HBHB"
/c: will display “C ” followed by the value of the text variable
/python: will display " Python " followed by the value of text variable --
    has default value of "is cool"
strict_slashes=False in route
"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id=None):
    """displays 'Hello HBNB!'"""
    states = [states for states in storage.all(State).values()]
    return_state = None
    if id:
        for state in states:
            if state.id == id:
                return_state = state
    return render_template('9-states.html', state=return_state)


@app.route("/cities_by_states", strict_slashes=False)
def states_city_list():
    """displays 'Hello HBNB!'"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/", strict_slashes=False)
def states_list():
    """displays 'Hello HBNB!'"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(cont):
    """remove the current sql alchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
