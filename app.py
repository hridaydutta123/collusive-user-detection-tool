from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = "SCoRe"
blueprint = make_twitter_blueprint(
    api_key="HyFodXHKk8h4wFqWCMVVASVmb",
    api_secret="aEb76Hg3I80DEO6ls03Qq6lY1terCooGPVzQ78YxWJnn2xTJra",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    # return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"])
    # return render_template('pages/placeholder.about.html')
    # return redirect(url_for('/about'))
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')
if __name__ == "__main__":
    app.run()
