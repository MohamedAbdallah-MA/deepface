# 3rd parth dependencies
from flask import Flask
from deepface.api.src.modules.core.routes import blueprint
import argparse
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    print(app.url_map)
    return app

if __name__ == "__main__":
    deepface_app = create_app()
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=os.getenv('DEFAULT_PORT'), help="Port of serving api")
    args = parser.parse_args()
    deepface_app.run(host="0.0.0.0", port=args.port)

# def create_online_app():
#     app = Flask(__name__)
#     app.register_blueprint(blueprint)
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-p", "--port", type=int, default=int(os.getenv('DEFAULT_PORT')), help="Port of serving api")
#     args = parser.parse_args()
#     app.run(host="0.0.0.0", port=args.port)
#     return app

# print('hi')
# print(blueprint)
# print('hi')
# print(app)
# print('hi')
# print('bye')