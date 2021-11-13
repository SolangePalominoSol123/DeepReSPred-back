from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

from views import api_blueprint
from models.endpoint import Endpoint
from models.parameter import Parameter
from models.file import File
from models.filexreq import Filexreq
from models.request import Request
from models.statusrequest import Statusrequest
from models.access import Access

def create_app(config_filename):
    app=Flask(__name__)
    app.config.from_object(config_filename)
    app.config['CORS_HEADERS'] = 'Content-Type'
    #CORS(app)
    CORS(app)#,resources={r"/*": {"origins": "*", "supports_credentials": True}})
    #cors.init_app(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
    db.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix="/api") #encapsulado del negocio

    return app