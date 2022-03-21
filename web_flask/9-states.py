"""States"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

states = storage.all(State)


@app.route("/states")
@app.route("/states/<id>")
def cities_list(id=None):
    return render_template('8-cities_by_states.html', states=states, id=id)


@app.teardown_appcontext
def teardown():
    storage.close()

app.run(host="0.0.0.0")