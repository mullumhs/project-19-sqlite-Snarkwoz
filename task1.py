import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               director TEXT,
               year INTEGER,
               genre TEXT,
               rating FLOAT    
)
''')

movie = ('The Dark Knight','Christopher Nolan',2008,'Action, Crime, Drama',9.0)
cursor.execute(f'''
INSERT INTO movies (title, director, year, genre, rating)
VALUES ('The Dark Knight','Christopher Nolan',2008,'Action, Crime, Drama',9.0)
''')

"""
cursor.execute('''
INSERT INTO movies (title,director,year,rating)
               VALUES (?,?,?,?,?)
''') ('The Dark Knight','Christopher Nolan',2008,'Action, Crime, Drama',9.0)
"""

cursor.execute('''
SELECT * FROM movies;
''')
all_movies = cursor.fetchall()
for movie in all_movies:
    print(movie)

conn.commit()
conn.close()