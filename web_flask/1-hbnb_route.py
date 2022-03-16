#!/usr/bin/python3
"""
Starting a Flask web application thats different than 1?
"""
from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """
        dispalys Hello HBHB!
        """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """
        Displays HBNB
        """
        return "HBNB"

    app.run('0.0.0.0')
