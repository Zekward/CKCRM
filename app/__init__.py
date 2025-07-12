from flask import Flask
from app.routes.dashboard import views
import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(base_dir, '..', 'templates')

    app = Flask(__name__, template_folder=template_path)
    app.register_blueprint(views)
    return app