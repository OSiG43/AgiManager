# Contient toutes les fonctions qui feront des requetes concernant agilog à la base de données
import sqlite3 as lite
from agimanager.db_utils import get_db


def getAllStock():
    con= get_db()
    cur=con.cursor()
    cur.execute('SELECT nom_piece, id_piece, quantite, seuil_commande FROM Stock_Agilog JOIN Pieces ON Pieces.ref = Stock_Agilog.id_piece')
    lignes=cur.fetchall()
    return(lignes)

def getPieceList() :
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, ref, nom_piece FROM Pieces')
    lignes = cur.fetchall()
    return (lignes)
def getKitList():
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, nom_kit FROM Kits')
    lignes = cur.fetchall()
    return (lignes)

def getPiecesKit(id_kit) :
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT id_kit, id_piece, quantié FROM Composition_kit WHERE id_kit = ?", {id_kit})
    lignes = cur.fetchall()
    return (lignes)

def getAllKitCmd():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT id_kit, h_envoi, h_recep FROM Commande_kit")
    lignes = cur.fetchall()
    return (lignes)