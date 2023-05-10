# Fichier qui contient toutes les vues propre à agilean
from flask import Blueprint, render_template, jsonify

agilean_bp = Blueprint('agilean', __name__, template_folder='../templates/agilean', static_folder='static')


@agilean_bp.route('/cmds_ajax')
def cmds_ajax():
    from agimanager.request import getAllKitCmd
    liste_cmds = getAllKitCmd()

    return jsonify(list(liste_cmds.values()))


@agilean_bp.route('/suivi_cmd')
def suivi_cmd():
    from agimanager.request import getAllKitCmd
    liste_cmds = getAllKitCmd()

    print(liste_cmds)
    return render_template('suivi_commandes.html', liste_cmds=liste_cmds)

@agilean_bp.route('/agilean_cmd')
def agilean_cmd():


    return render_template('agilean_cmd.html')
