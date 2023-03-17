# Fichier qui contient toutes les vues propre à agilean
from flask import Blueprint, render_template

agilean_bp = Blueprint('agilean', __name__, template_folder='../templates/agilean', static_folder='static')


@agilean_bp.route('/test')
def test():
    return render_template('test_agilean.html')
