from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbhb():
    return "HBNB"

@app.route("/c/<text>")
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))

@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)

app.run(host="0.0.0.0")
