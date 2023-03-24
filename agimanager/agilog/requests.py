# Contient toutes les fonctions qui feront des requetes concernant agilog à la base de données
import sqlite3 as lite
from agimanager.db_utils import get_db


def getAllStock():
    con= get_db()
    cur=con.cursor()
    cur.execute('SELECT ID_piece, Quantité FROM Stock_Agilog')
    lignes=cur.fetchall()

def getPieceList() :
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, ref, nom_piece FROM Pieces')
    lignes = cur.fetchall()

def getKitList():
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id, nom_kit FROM Kits')
    lignes = cur.fetchall()

def getPiecesKit(id_kit) :
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT id_kit, id_piece, quantié FROM Composition_kit WHERE id_kit = {id_kit}")
    lignes = cur.fetchall()

