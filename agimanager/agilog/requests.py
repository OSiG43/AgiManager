# Contient toutes les fonctions qui feront des requetes concernant agilog à la base de données
import sqlite3 as lite
from agimanager.db_utils import get_db


def getAllStock():
    con= get_db()
    cur=con.cursor()
    cur.execute('SELECT id_piece, quantite FROM Stock_Agilog')
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

def getStatKitCmd():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT count(Composition_leanCmd_kit.id_cmd), avg(h_achat-h_recep), Composition_leanCmd_kit.quantite FROM Commande_Agilean JOIN Composition_leanCmd_kit ON Commande_Agilean.id = Composition_leanCmd_kit.id_cmd WHERE Commande_Agilean.id = Composition_leanCmd_kit.id_cmd")
    lignes = cur.fetchall()
    return (lignes)


def getStatPieceCmd():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT count(Composition_leanCmd_piece.id_cmd), avg(h_achat-h_recep), Composition_leanCmd_piece.quantite FROM Commande_Agilean JOIN Composition_leanCmd_piece ON Commande_Agilean.id = Composition_leanCmd_piece.id_cmd WHERE Commande_Agilean.id = Composition_leanCmd_piece.id_cmd")
    lignes = cur.fetchall()
    return (lignes)