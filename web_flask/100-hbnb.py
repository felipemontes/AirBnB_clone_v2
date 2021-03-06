#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def closing(error):
    """closes session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """ function that renders airbnb template"""
    state = storage.all('State')
    amenities = storage.all('Amenity')
    place = storage.all('Place')
    return render_template('100-hbnb.html', state=state,
                           amenities=amenities, place=place)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
