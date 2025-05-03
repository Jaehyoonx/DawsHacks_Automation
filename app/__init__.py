from flask import Flask
from config import ConfigDev
from app.main.routes import main_bp

def create_app():
    """App function"""
    app = Flask(__name__)
    app.config.from_object(ConfigDev)

    app.register_blueprint(main_bp)

    return app