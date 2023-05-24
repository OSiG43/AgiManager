
#Fichier d'initialisation de l'app flask
import os
import shutil
import time

from flask import Flask, render_template, url_for, redirect, g, current_app

from agigreen.agigreen import agigreen_bp
from agilean.agilean import agilean_bp
from agilog.agilog import agilog_bp


app = Flask(__name__)

#On importe les vues
app.register_blueprint(agilog_bp, url_prefix='/agilog')
app.register_blueprint(agilean_bp, url_prefix='/agilean')
app.register_blueprint(agigreen_bp, url_prefix='/agigreen')


@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.route('/admin')
def admin():
    from timer_utils import timer_get_elapsed_time, is_timer_running
    elapsed_time = timer_get_elapsed_time()
    started = is_timer_running()
    return render_template('admin.html', started=started, elapsed_time=timer_get_elapsed_time())

@app.route('/start_timer')
def start_timer():
    from timer_utils import timer_start
    timer_start()

    return redirect(url_for('admin'))

@app.route('/pause_timer')
def pause_timer():
    from timer_utils import timer_pause
    timer_pause()
    return redirect(url_for('admin'))

@app.route('/reset_timer')
def reset_timer():
    from timer_utils import timer_reset
    timer_reset()
    return redirect(url_for('admin'))

@app.route('/copy_prefilled_bdd')
def copy_prefilled_bdd():
    db = get_db()
    with app.open_resource('schema_rempli.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    return redirect(url_for('admin'))

@app.route('/copy_empty_bdd')
def copy_empty_bdd():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

    return redirect(url_for('admin'))

@app.route('/init_stock')
def init_stock():
    #on met le stock de toutes les pièces à 100
    from request import getPieceList, AddStock, clearStock, setSeuils
    pieces = getPieceList()
    clearStock()
    for piece in pieces:
        AddStock(piece["id"], 100)
        setSeuils(piece["id"], 99, 1)
    return redirect(url_for('admin'))

#On lance l'application
if __name__ == '__main__':
    from db_utils import init_db, get_db

    init_db()
    app.run(debug=True, port=5678)

