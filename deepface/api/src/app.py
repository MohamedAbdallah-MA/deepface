# 3rd parth dependencies
from flask import Flask
from deepface.api.src.modules.core.routes import blueprint
from pyngrok import ngrok
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    print(app.url_map)
    return app

def get_public_url(port):
    ngrok.set_auth_token(os.getenv('NGROK_AUTH_TOKEN'))
    public_url = ngrok.connect(port)
    print("ngrok public url is")
    print(public_url)
