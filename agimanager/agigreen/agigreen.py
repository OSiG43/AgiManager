# Fichier qui contient toutes les vues propre à agilean
from flask import Blueprint, render_template

agigreen_bp = Blueprint('agigreen', __name__, template_folder='../templates/agigreen', static_folder='static')


@agigreen_bp.route('/test')
def test():
    return render_template('test_agigreen.html')
