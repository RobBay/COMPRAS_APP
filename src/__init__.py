from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "¡Hola desde la estructura modular con src! 🚀"

    return app
