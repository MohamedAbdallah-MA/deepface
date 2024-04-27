# 3rd parth dependencies
from flask import Flask
from deepface.api.src.modules.core.routes import blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    print(app.url_map)
    return app

# print('hi')
# print(blueprint)
# print('hi')
# print(app)
# print('hi')
# print('bye')