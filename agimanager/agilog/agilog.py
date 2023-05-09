# Fichier qui contient toutes les vues propre à agilog
from flask import Blueprint, render_template, request, jsonify

agilog_bp = Blueprint('agilog', __name__, template_folder='../templates/agilog', static_folder='static')

@agilog_bp.route('/cmds_ajax')
def cmds_ajax():
    from agimanager.request import getAllKitCmd
    liste_cmds = getAllKitCmd('status="Reçu", status="Envoyée"')

    return jsonify(list(liste_cmds.values()))

@agilog_bp.route('/suivi')
def agilogcmd():
    from agimanager.request import getAllKitCmd
    liste_cmds = getAllKitCmd('status="Reçu", status="Envoyée"')
    return render_template('agilog_suivi_cmd.html', liste_cmds=liste_cmds)

@agilog_bp.route("/receive_cmd", methods=('POST',))
def receive_cmd():
    from agimanager.request import changeAgileanCmdStatus
    if changeAgileanCmdStatus(request.json["id"], request.json["status"]):
        return "OK"
    else:
        return "Error"
@agilog_bp.route('/stock')
def stock():
    return render_template('stock.html')

@agilog_bp.route('/stock')
def stock():
    return render_template('stock.html')
