from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api

app = Flask(__name__)
api_restful = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

cors = CORS()

bcrypt = Bcrypt(app)

from app.api.models import users
from app.api.views import users

def create_app(script_info=None):
    # instantiate the app

    cors.init_app(app)

    with app.test_request_context():
        db.create_all()

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}  # tirei um 'db': db
    return app
