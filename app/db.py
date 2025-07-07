import sqlite3
from datetime import datetime
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

db_path = os.path.join(DATA_DIR, "trips.db")
conn = sqlite3.connect(db_path)

def get_connection():
    return sqlite3.connect("trips.db", check_same_thread=False)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            moving_time INTEGER,
            stopped_time INTEGER,
            cost REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_trip(moving_time, stopped_time, cost):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trips (date, moving_time, stopped_time, cost)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now().isoformat(), moving_time, stopped_time, cost))
    conn.commit()
    conn.close()

def get_trip_history():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM trips ORDER BY date DESC", conn)
    conn.close()
    return df
