"""States_List"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

states = storage.all(State)

@app.route("/states_list")
def states_list():
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown():
    storage.close()

app.run(host="0.0.0.0")
