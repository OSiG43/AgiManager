
#Fichier d'initialisation de l'app flask
from flask import Flask, render_template

from agimanager.agigreen.agigreen import agigreen_bp
from agimanager.agilean.agilean import agilean_bp
from agimanager.agilog.agilog import agilog_bp


app = Flask(__name__)

#On importe les vues
app.register_blueprint(agilog_bp, url_prefix='/agilog')
app.register_blueprint(agilean_bp, url_prefix='/agilean')
app.register_blueprint(agigreen_bp, url_prefix='/agigreen')


@app.route('/')
def accueil():
    return render_template('accueil.html')



#On lance l'application
if __name__ == '__main__':
    from agimanager.db_utils import init_db
    init_db()
    app.run(debug=True, port=5678)

