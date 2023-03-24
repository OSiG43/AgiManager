# Contient toutes les fonctions qui feront des requetes concernant agilog à la base de données
import sqlite3 as lite


def getStock():
    con=lite.connect('BDD_OREXA.db')
    con.row_factory=lite.Row
    cur=con.cursor()
    cur.execute('SELECT ID_piece, Quantité FROM Stock Agilog')
    lignes=cur.fetchall()
    con.close()