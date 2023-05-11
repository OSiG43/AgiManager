from math import floor

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
    cur.execute('SELECT id, ref, nom FROM Pieces')
    lignes = cur.fetchall()
    return lignes

def getKitList():
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, nom FROM Kits')
    lignes = cur.fetchall()
    return lignes

def getPiecesKit(id_kit) :
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT id_kit, id_piece, quantié FROM Composition_kit WHERE id_kit = ?", {id_kit})
    lignes = cur.fetchall()
    return lignes

def getAllKitCmd(order_by="status='Reçu'"):
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM Commande_Agilean ORDER BY {order_by}")
    lignes = cur.fetchall()

    # On initialise la liste des commandes avec des dictionnaires vides pour chaque commande c'est à dire chaque
    # id distinct
    # Il faut faire ça car la requete sql renvoie plusieurs ligne associé à la même commande dès lors qu'il y a
    # plusieurs kits dans la commande. Cette requete à l'avantage de permettre la récupèration de toutes les infos
    # en une seule requete
    unique_cmds = list(dict.fromkeys([cmd["id"] for cmd in lignes]).keys())
    liste_cmds = {id: {} for id in unique_cmds}

    for cmd in lignes:
        #On récupère la liste des kits dans la commande
        querry = "SELECT id_kit, Kits.nom, quantite FROM Composition_leanCmd_kit JOIN Kits on id_kit=Kits.id WHERE id_cmd = ?"
        cur.execute(querry, (cmd["id"],))
        kits = cur.fetchall()

        #on récupère la listes des pièces dans la commande
        querry = "SELECT id_piece, Pieces.nom, quantite FROM Composition_leanCmd_piece JOIN Pieces on id_piece=Pieces.id WHERE id_cmd = ?"
        cur.execute(querry, (cmd["id"],))
        pieces = cur.fetchall()

        liste_cmds[cmd["id"]]["id"] = cmd["id"]
        liste_cmds[cmd["id"]]["status"] = cmd["status"]
        liste_cmds[cmd["id"]]["h_achat"] = cmd["h_achat"]
        liste_cmds[cmd["id"]]["h_recep"] = cmd["h_recep"]
        liste_cmds[cmd["id"]]["kits"] = [dict(kit) for kit in kits]
        liste_cmds[cmd["id"]]["pieces"] = [dict(piece) for piece in pieces]

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


def addAgileanCmd(kits_list, pieces_list):
    from agimanager.timer_utils import timer_get_elapsed_time
    # Connexion à la base de données
    con = get_db()
    cursor = con.cursor()

    # Insertion de la commande dans la table "Commande_Agilean"
    query_cmd = "INSERT INTO Commande_Agilean (h_achat) VALUES (?)"
    cursor.execute(query_cmd, (floor(timer_get_elapsed_time()),))
    cmd_id = cursor.lastrowid

    # Insertion des kits dans la table "Composition_leanCmd_kit"
    for kit in kits_list:
        query_option = "INSERT INTO Composition_leanCmd_kit (id_cmd, id_kit, quantite) VALUES (?, ?, ?)"
        cursor.execute(query_option, (cmd_id, kit["id"], kit["quantite"]))

    # Insertion des kits dans la table "Composition_leanCmd_piece"
    for piece in pieces_list:
        query_option = "INSERT INTO Composition_leanCmd_piece (id_cmd, id_piece, quantite) VALUES (?, ?, ?)"
        cursor.execute(query_option, (cmd_id, piece["id"], piece["quantite"]))

    # Validation de la transaction
    con.commit()

    return cmd_id

def changeAgileanCmdStatus(cmd_id, status):
    from agimanager.timer_utils import timer_get_elapsed_time
    h_to_update = {"En traitement": "h_production", "Envoyée": "h_envoi", "Reçu": "h_recep"}[status]
    con = get_db()
    cur = con.cursor()
    cur.execute(f"UPDATE Commande_Agilean SET (status,{h_to_update}) = (?,?) WHERE id = ?", (status, floor(timer_get_elapsed_time()), cmd_id))
    con.commit()
    #On renvoi 0 si erreur 1 si tout bon.
    return cur.rowcount

