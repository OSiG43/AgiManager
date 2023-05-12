# Fichier qui contient toutes les vues propre à agilean
from flask import Blueprint, render_template, jsonify, request

agigreen_bp = Blueprint('agigreen', __name__, template_folder='../templates/agigreen', static_folder='static')


@agigreen_bp.route('/suivi_cmd')
def suivi_cmd():
    from agimanager.request import getAllAgigreenCmd
    liste_cmds = getAllAgigreenCmd('status="Livrée"')
    return render_template('agigreen_suivi_cmd.html', liste_cmds=liste_cmds)

@agigreen_bp.route('/cmds_ajax')
def cmds_ajax():
    from agimanager.request import getAllAgigreenCmd
    liste_cmds = getAllAgigreenCmd('status="Reçu", status="Envoyée"')

    return jsonify(list(liste_cmds.values()))

@agigreen_bp.route("/receive_cmd", methods=('POST',))
def receive_cmd():
    from agimanager.request import setAgigreenCmdSent
    if setAgigreenCmdSent(request.json["id"]):
        return "OK"
    else:
        return "Error"