from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_login import LoginManager

app = Flask(__name__)
api_restful = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

cors = CORS()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from app.api.models import users
from app.api.views import users

from app.api.models import news
from app.api.views import news

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
