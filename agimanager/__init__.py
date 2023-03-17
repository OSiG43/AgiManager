
#Fichier d'initialisation de l'app flask

def create_app():
    app = Flask(__name__)

    app.config.update(config)  # Override with passed config
    return app
