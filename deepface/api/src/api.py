import argparse
import app
import os

if __name__ == "__main__":
    deepface_app = app.create_app()
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=int(os.getenv('DEFAULT_PORT')), help="Port of serving api")
    args = parser.parse_args()
    # app.get_public_url(port=args.port)
    deepface_app.run(host="0.0.0.0", port=args.port)
