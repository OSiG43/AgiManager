from agimanager.db_utils import get_db

def getAllStock():
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id_piece, quantite FROM Stock_Agilog')
    lignes = cur.fetchall()
    return lignes

def getPieceList() :
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, ref, nom_piece FROM Pieces')
    lignes = cur.fetchall()
    return lignes
def getKitList():
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, nom_kit FROM Kits')
    lignes = cur.fetchall()
    return lignes

def getPiecesKit(id_kit) :
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT id_kit, id_piece, quantié FROM Composition_kit WHERE id_kit = ?", {id_kit})
    lignes = cur.fetchall()
    return lignes

def getAllKitCmd():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT cmd.*, compo.id_kit, compo.quantite FROM Commande_Kit as cmd JOIN Composition_cmd_kit as compo on id_cmd=cmd.id ORDER BY cmd.status='Reçu'")
    lignes = cur.fetchall()

    # On initialise la liste des commandes avec des dictionnaires vides pour chaque commande c'est à dire chaque
    # id distinct
    # Il faut faire ça car la requete sql renvoie plusieurs ligne associé à la même commande dès lors qu'il y a
    # plusieurs kits dans la commande. Cette requete à l'avantage de permettre la récupèration de toutes les infos
    # en une seule requete
    unique_cmds = list(dict.fromkeys([cmd["id"] for cmd in lignes]).keys())
    liste_cmds = {id: {"kits": []} for id in unique_cmds}

    for cmd in lignes:
        liste_cmds[cmd["id"]]["id"] = cmd["id"]
        liste_cmds[cmd["id"]]["status"] = cmd["status"]
        liste_cmds[cmd["id"]]["h_envoi"] = cmd["h_envoi"]
        liste_cmds[cmd["id"]]["h_recep"] = cmd["h_recep"]
        liste_cmds[cmd["id"]]["kits"].append({"id_kit": cmd["id_kit"], "quantite": cmd["quantite"]})

    return liste_cmds


def getStock(id_piece):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour récupérer le stock de la pièce
    query = "SELECT quantite FROM Stock_Agilog WHERE id_piece = ?"
    cursor.execute(query, (id_piece,))
    result = cursor.fetchone()

    # Vérification que la pièce a été trouvée
    if result is None:
        return "La pièce avec l'ID " + str(id_piece) + " n'a pas été trouvée dans le stock Agilog."
    else:
        return result[0]


def AddOption(ref, nom, id_piece=None):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour insérer une nouvelle option dans la table "Option"
    query = "INSERT INTO Option (code_option, id_piece, nom_option) VALUES (?, ?, ?)"
    cursor.execute(query, (ref, id_piece, nom))

    # Validation de la transaction
    con.commit()


    # Message de confirmation
    return "L'option avec le code " + str(ref) + " a été ajoutée à la base de données."


def AddKit(nom):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour insérer un nouveau kit dans la table "Kits"
    query = "INSERT INTO Kits (nom_kit) VALUES (?)"
    cursor.execute(query, (nom,))

    # Validation de la transaction
    con.commit()

    # Message de confirmation
    return "Le kit avec le nom " + str(nom) + " a été ajouté à la base de données."


def AddPiece(ref, nom):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour insérer une nouvelle pièce dans la table "Pieces"
    query = "INSERT INTO Pieces (id_piece, designation) VALUES (?, ?)"
    cursor.execute(query, (ref, nom))

    # Validation de la transaction
    con.commit()

    # Message de confirmation
    return "La pièce avec l'id " + str(ref) + " a été ajoutée à la base de données."


def AddPieceInKit(id_kit, id_piece, qts):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour insérer une nouvelle entrée dans la table "composition_kit"
    query = "INSERT INTO composition_kit (id_kit, id_piece, quantite) VALUES (?, ?, ?)"
    cursor.execute(query, (id_kit, id_piece, qts))

    # Validation de la transaction
    con.commit()

    # Message de confirmation
    return "L'entrée avec l'id_kit " + str(id_kit) + " et l'id_piece " + str(
        id_piece) + " a été ajoutée à la base de données."


def AddStock(id_piece, qts, seuil_cmd):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Exécution de la requête SQL pour insérer une nouvelle entrée dans la table "stock_agilog"
    query = "INSERT INTO stock_agilog (id_piece, quantite, seuil_commande) VALUES (?, ?, ?)"
    cursor.execute(query, (id_piece, qts, seuil_cmd))

    # Validation de la transaction
    con.commit()


    # Message de confirmation
    return "L'entrée avec l'id_piece " + str(id_piece) + ", la quantité " + str(
        qts) + " et le seuil de commande " + str(seuil_cmd) + " a été ajoutée à la base de données."


def addKitCmd(id_kit, options):
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Insertion de la commande dans la table "commande_kit"
    query_cmd = "INSERT INTO commande_kit (id_kit, h_recept, h_envoi) VALUES (?, ?, ?)"
    cursor.execute(query_cmd, (id_kit, None, None))
    cmd_id = cursor.lastrowid

    # Insertion des options dans la table "composition_option"
    for option_id in options:
        query_option = "INSERT INTO composition_option (id_commande, id_option) VALUES (?, ?)"
        cursor.execute(query_option, (cmd_id, option_id))

    # Validation de la transaction
    con.commit()

    # Message de confirmation
    return "La commande avec l'id_kit " + str(id_kit) + " et les options " + str(
        options) + " a été ajoutée à la base de données."

