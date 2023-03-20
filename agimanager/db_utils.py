import os
import sqlite3

from flask import g

from agimanager.app import app

DATABASE = 'database.db'


def get_db():
    # on vérifie si la base de données est déjà ouverte
    # g est un objet qui est stocké dans le contexte de l'app flask
    # équivalent de faire une variable globale
    db = getattr(g, '_database', None)
    if db is None:
        # on vérifie si la base de données existe
        if os.path.exists(DATABASE):
            db = g._database = sqlite3.connect(DATABASE)
            db.row_factory = sqlite3.Row
        else:
            # on lance une exception si la base de données n'existe pas
            raise FileNotFoundError("La base de données n'existe pas")
    return db


# On ferme la connexion à la base de données
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# On vérifie si la base de données existe, si elle n'existe pas on la crée
# Si elle n'existe pas on la crée en utilisant le fichier schema.sql qui contient
# les requêtes pour créer les tables
def init_db():
    if os.path.exists(DATABASE):
        return
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


