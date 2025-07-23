# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 12:02:20 2025

@author: henim
"""

import sqlite3

# Connexion (ou création) à la base de données SQLite
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# Suppression de la table si elle existe déjà
cur.execute('DROP TABLE IF EXISTS books')

# Création de la table 'books'
cur.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        "first sentence" TEXT,
        published TEXT
    )
''')

# Insertion des livres
books = [
    (0, 'A Fire Upon the Deep', 'Vernor Vinge',
     'The coldsleep itself was dreamless.', '1992'),

    (1, 'The Ones Who Walk Away From Omelan', 'Ursula K. Le Guin',
     'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', '1973'),

    (2, 'Dhalgren', 'Samuel R. Delany',
     'to wound the autumnal city.', '1975')
]

cur.executemany('''
    INSERT INTO books (id, title, author, "first sentence", published)
    VALUES (?, ?, ?, ?, ?)
''', books)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("La base de données 'books.db' a été initialisée avec succès.")
