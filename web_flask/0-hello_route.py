"""Hello Route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "<p>Hello HBNB!</p>"

app.run(host="0.0.0.0")
