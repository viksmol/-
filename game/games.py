import sqlite3
import json
from datetime import datetime

def parse_data_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

conn = sqlite3.connect('staff.db')
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS game (
    vergil_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vergil_name TEXT,               
    vergil_price TEXT,
    nationality TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS proget (
    proget_id INTEGER PRIMARY KEY AUTOINCREMENT,
    proget_name TEXT,
    proget_data TEXT
);
""")

with open("C:\\Users\\Admin\\Desktop\\game\\games.json", "r", encoding="utf-8") as f:
    games = json.load(f)

for game in games:
    # Вставка в таблицю game
    cursor.execute("""
        INSERT INTO game (
            vergil_name, vergil_price, nationality
        ) VALUES (?, ?, ?)
    """, (
        game["vergil_name"],
        game["vergil_price"],
        game["nationality"]
    ))

    # Отримуємо ID тільки-що доданої гри
    game_id = cursor.lastrowid

    # Вставка в таблицю proget
    cursor.execute("""
        INSERT INTO proget (
            proget_name, proget_data
        ) VALUES (?, ?)
    """, (
        game["vergil_name"],
        str(parse_data_safe(game.get("vergil")))
    ))

conn.commit()
conn.close()
