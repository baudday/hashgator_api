from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:baseba77@localhost/hashgator'
db = SQLAlchemy(app)
api = restful.Api(app)

import hashgator_api.routes
