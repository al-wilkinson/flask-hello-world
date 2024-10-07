# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"<h1>Hello world, Flask on Azure Web App!</h1><hr/>Current clock time is: {datetime.datetime.utcnow()}"



