import sqlite3
from const import DB_PATH


def execute_request(request):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    val = cursor.execute(request).fetchall()

    conn.commit()

    return val
