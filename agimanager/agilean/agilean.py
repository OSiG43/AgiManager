# Fichier qui contient toutes les vues propre à agilean
from flask import Blueprint, render_template, jsonify, request

agilean_bp = Blueprint('agilean', __name__, template_folder='../templates/agilean', static_folder='static')


@agilean_bp.route('/cmds_ajax')
def cmds_ajax():
    from agimanager.request import getAllAgileanCmd
    liste_cmds = getAllAgileanCmd()

    return jsonify(list(liste_cmds.values()))


@agilean_bp.route('/suivi_cmd',methods=('GET', 'POST'))
def suivi_cmd():
    from agimanager.request import getAllAgileanCmd, getKitList, getPieceList, addAgileanCmd

    if request.method == "POST":
        #request.form est de la forme suivante : ImmutableMultiDict([('kit-1', '5'), ('kit-qts-1', '1'),('kit-1683824743687', '2'), ('kit-qts-1683824743687', '3')])
        # ici, le kit 5 est commandé en 1 exemplaire et le kit 2 est commandé en 3 exemplaires
        #On récupère la liste des kits sous la forme [{"id": "5", "qts": "1"}, {"id": "2", "qts": "3"}]
        kit_list = []
        for key, value in request.form.items():
            if value == "-1":
                continue
            if key.startswith("kit-"):
                index = key.lstrip("kit-")
                kit_list.append({"id": value, "quantite": request.form[f"qts-kit-{index}"]})

        #Pareil avec les pieces
        piece_list = []
        for key, value in request.form.items():
            if value == "-1":
                continue
            if key.startswith("piece-"):
                index = key.lstrip("piece-")
                piece_list.append({"id": value, "quantite": request.form[f"qts-piece-{index}"]})

        #Si il y a des kits ou des pièces à commander, on les ajoute à la base de donnée
        if len(kit_list) != 0 or len(piece_list) != 0:
            addAgileanCmd(kit_list, piece_list)

    liste_cmds = getAllAgileanCmd()
    liste_kits = getKitList()
    liste_pieces = getPieceList()

    return render_template('gestion_commandes.html', liste_cmds=liste_cmds, liste_kits=liste_kits, liste_pieces=liste_pieces)

@agilean_bp.route("/receive_cmd", methods=('POST',))
def receive_cmd():
    from agimanager.request import changeAgileanCmdStatus
    if changeAgileanCmdStatus(request.json["id"], "Reçu"):
        return "OK"
    else:
        return "Error"


