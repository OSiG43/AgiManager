import time

from flask import g




def timer_start():
    from db_utils import get_db

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM timer")

    timer = cur.fetchone()
    if timer is None:
        cur.execute("INSERT INTO timer (start_timestamp) VALUES (?)", (time.time(),))
    else:
        cur.execute("UPDATE timer SET (pause_elapsed_time, pause_timestamp) = (pause_elapsed_time + ? - pause_timestamp, NULL)", (time.time(),))
    con.commit()

def is_timer_running():
    from db_utils import get_db

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT pause_timestamp FROM timer")
    timer = cur.fetchone()
    if timer is None:
        return False
    else:
        if timer["pause_timestamp"] is None:
            return True
    return False



def timer_pause():
    from db_utils import get_db

    con = get_db()
    cur = con.cursor()
    cur.execute("UPDATE timer SET pause_timestamp = ?", (time.time(),))
    con.commit()


def timer_reset():
    from db_utils import get_db

    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM timer")
    con.commit()


def timer_get_elapsed_time():
    from db_utils import get_db

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM timer")
    timer = cur.fetchone()
    if timer is None:
        return 0
    else:
        if timer["pause_timestamp"] is None:
            return time.time() - timer["start_timestamp"] - timer["pause_elapsed_time"]
        else:
            return timer["pause_timestamp"] - timer["start_timestamp"] - timer["pause_elapsed_time"]
