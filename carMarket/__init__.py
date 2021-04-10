from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # this returns a WSGI instance
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///carMarketDB.db"
db = SQLAlchemy(app)


def import_essentials():
    from carMarket import routes  # otherwise __init__.py can not find created routes
    from carMarket import models


import_essentials()
