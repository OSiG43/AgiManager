
#Fichier d'initialisation de l'app flask
import time

from flask import Flask, render_template, url_for, redirect, g

from agimanager.agigreen.agigreen import agigreen_bp
from agimanager.agilean.agilean import agilean_bp
from agimanager.agilog.agilog import agilog_bp


app = Flask(__name__)

#On importe les vues
app.register_blueprint(agilog_bp, url_prefix='/agilog')
app.register_blueprint(agilean_bp, url_prefix='/agilean')
app.register_blueprint(agigreen_bp, url_prefix='/agigreen')


@app.route('/')
def accueil():
    from agimanager.agilog.requests import getAllStock
    stock = getAllStock()
    return render_template('stock.html', stock = stock)

@app.route('/admin')
def admin():
    from agimanager.timer_utils import timer_get_elapsed_time, is_timer_running
    elapsed_time = timer_get_elapsed_time()
    started = is_timer_running()
    return render_template('admin.html', started=started, elapsed_time=timer_get_elapsed_time())

@app.route('/start_timer')
def start_timer():
    from agimanager.timer_utils import timer_start
    timer_start()

    return redirect(url_for('admin'))

@app.route('/pause_timer')
def pause_timer():
    from agimanager.timer_utils import timer_pause
    timer_pause()
    return redirect(url_for('admin'))

@app.route('/reset_timer')
def reset_timer():
    from agimanager.timer_utils import timer_reset
    timer_reset()
    return redirect(url_for('admin'))

#On lance l'application
if __name__ == '__main__':
    from agimanager.db_utils import init_db
    init_db()
    app.run(debug=True, port=5678)

