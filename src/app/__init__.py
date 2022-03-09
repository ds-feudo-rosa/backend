from flask_cors import CORS
from flask import Flask
import os
from app.api.views.users import user_blueprint


cors = CORS()

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    cors.init_app(app)
    app.register_blueprint(user_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}  # tirei um 'db': db
    return app
