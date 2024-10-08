from flask import Flask, render_template
from flask_session import Session
from src.core.bcrypt import bcrypt
from src.web.config import config
from src.web.controllers.users import bp as blueprint_users
from src.web.controllers.auth import bp as blueprint_auth
from src.web.helpers import handler
from src.core import database
from src.core import seed

session = Session()

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    
    #Registros blueprint
    app.register_blueprint(blueprint_users)
    app.register_blueprint(blueprint_auth)

    #Init database
    database.init_app(app)

    #Init session
    session.init_app(app)

    #Init bcrypt
    bcrypt.init_app(app)

    # Error handler
    app.register_error_handler(404, handler.not_found_error)

    #Registrar comandos asociados a la base de datos
    @app.cli.command(name="reset-db")
    def reset_db():
        database.reset()
        
    @app.cli.command(name="seed-basic")
    def init_seed():
        seed.run()
        
    return app