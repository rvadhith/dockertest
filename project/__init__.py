from flask import Flask
from routes.routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    #commented    
    return app
