#!/usr/bin/python3
"""importando librerias"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHtn():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    return 'HBNB'


@app.route('/c/<name>', strict_slashes=False)
def cprofile(name):
    return "C " + str(name).replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def aprofile(text):
    return "Python " + str(text).replace("_", " ")

"""condicion"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
