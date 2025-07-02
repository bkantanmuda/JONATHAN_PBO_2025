import sqlite3
from pathlib import Path

def get_connection():
    db_path = Path("flipper_data.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(sql, params=None):
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute(sql, params or ())
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            print("DB Error:", e)
            return None

def fetch_query(sql, params=None, fetch_all=True):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql, params or ())
        return cur.fetchall() if fetch_all else cur.fetchone()

def get_dataframe(sql, params=None):
    import pandas as pd
    with get_connection() as conn:
        return pd.read_sql_query(sql, conn, params=params or ())