from flask import Flask
from src.models import Base, engine
from src.models.categories import Category

def create_app():
    app = Flask(__name__)

    
    Base.metadata.create_all(bind=engine)

   

    @app.route("/")
    def home():
        return "¡Hola desde la estructura modular con src! 🚀"

    return app
