"""Bus Ratings."""
import os

from jinja2 import StrictUndefined

from flask import Flask, jsonify,render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from sqlalchemy import func, desc

from model import Item, Order, User, connect_to_db, db

app = Flask(__name__)

app.secret_key = "d56f932859da1fb84bd072f5be866afc4bae33d59f3bfc72ddbe76625d841e72"

app.jinja_env.undefined = StrictUndefined



@app.route('/')
def home():
    """Homepage"""

    return render_template("home.html")


@app.route('/about')
def about():
    """About the band"""

    return render_template("about.html")

@app.route('/photos')
def photos():
    """Band Photography"""

    return render_template("photos.html")




if __name__ == "__main__":

    # connect_to_db(app, os.environ.get("DATABASE_URL"))
    #
    # # Create the tables we need from our models (if they already
    # # exist, nothing will happen here, so it's fine to do this each
    # # time on startup)
    # # db.create_all(app=app)
    #
    # DEBUG = "NO_DEBUG" not in os.environ
    # PORT = int(os.environ.get("PORT", 5000))
    #
    # app.run(host="0.0.0.0", port=PORT, debug=DEBUG)



    ####################################

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(port=5000, host="0.0.0.0")
