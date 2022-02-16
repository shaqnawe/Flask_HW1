from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register the blueprints
    from app.blueprints.home import bp as home
    from app.blueprints.main import bp as main
    app.register_blueprint(home)
    app.register_blueprint(main)
    
    return app