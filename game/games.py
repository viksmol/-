import sqlite3
import json
from datetime import datetime

# 🔧 Функція на випадок, якщо колись треба буде обробляти дати
def parse_date_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

# 📂 Підключення до бази даних
conn = sqlite3.connect("videogames.db")
cursor = conn.cursor()

# ✅ Увімкнення зовнішніх ключів
cursor.execute("PRAGMA foreign_keys = ON;")

# 🧱 Створення таблиці відеоігор
cursor.execute("""
CREATE TABLE IF NOT EXISTS videogames (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER,
    developer TEXT,
    budget REAL
);
""")

# 🧱 Створення таблиці з додатковою інформацією
cursor.execute("""
CREATE TABLE IF NOT EXISTS game_info (
    info_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    genre TEXT,
    rating REAL,
    platform TEXT,
    FOREIGN KEY (game_id) REFERENCES videogames(game_id) ON DELETE CASCADE
);
""")

# 📥 Завантаження даних із JSON-файлу
with open("videogames_data.json", "r", encoding="utf-8") as f:
    games = json.load(f)

# ➕ Додавання записів
for game in games:
    # 🎮 Вставка в таблицю videogames
    cursor.execute("""
        INSERT INTO videogames (title, release_year, developer, budget)
        VALUES (?, ?, ?, ?)
    """, (
        game["title"],
        game["release_year"],
        game["developer"],
        game["budget"]
    ))

    game_id = cursor.lastrowid  # 🔑 Отримання ID гри

    # 📊 Вставка жанру, рейтингу та платформи
    cursor.execute("""
        INSERT INTO game_info (game_id, genre, rating, platform)
        VALUES (?, ?, ?, ?)
    """, (
        game_id,
        game["genre"],
        game["rating"],
        game["platform"]
    ))

# 💾 Збереження змін і закриття
conn.commit()
conn.close()

print("✅ Дані про відеоігри успішно додано до бази даних.")
