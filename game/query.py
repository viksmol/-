import sqlite3

conn = sqlite3.connect("videogames.db")
cursor = conn.cursor()

def execute_query(query, params=()):
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Помилка при виконанні запиту: {e}")

print("\nДістаєло всі дані з таблиці 'videogames'")

execute_query("""
    SELECT *
    FROM videogames
""")

print("\nДістаєло назви і рік релізу дані з таблиці 'videogames'")

execute_query("""
    SELECT title, release_year
    FROM videogames
""")


print("\nДістаєло назви і бюджет релізу дані з таблиці 'videogames'")

execute_query("""
    SELECT title,  budget
    FROM videogames
""")

print("\nДістаєло назви рік компанія і бюджет релізу дані з таблиці 'videogames'")

execute_query("""
    SELECT title, release_year, developer, budget
    FROM videogames
""")

execute_query("""
    SELECT title, genre, platform
    FROM videogames
    INNER JOIN enrollment
    ON enrollment.gama_id = 
""")


conn.close()