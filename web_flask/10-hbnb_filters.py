#!/usr/bin/python3
"""Script to start a Flask web application
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
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnbFilters():
    """displays hbnb_filters.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities)


@app.teardown_appcontext
def teardown(cont):
    """remove the current sql alchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
