# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:48:19 2025

@author: henim
"""

import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Utilitaire : transforme les tuples en dictionnaires
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Page d'accueil simple
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Chinook API</h1>
<p>Une API prototype pour parcourir les artistes de la base Chinook.</p>'''

# Tous les artistes : GET /api/v1/resources/artists/all
@app.route('/api/v1/resources/artists/all', methods=['GET'])
def api_all_artists():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_artists = cur.execute('SELECT * FROM artists;').fetchall()
    conn.close()
    return jsonify(all_artists)

# Filtrage par id ou nom : GET /api/v1/resources/artists?id=1
@app.route('/api/v1/resources/artists', methods=['GET'])
def api_filter_artists():
    query_parameters = request.args
    artist_id = query_parameters.get('id')
    name = query_parameters.get('name')

    query = "SELECT * FROM artists WHERE"
    to_filter = []

    if artist_id:
        query += " ArtistId=? AND"
        to_filter.append(artist_id)
    if name:
        query += " Name LIKE ? AND"
        to_filter.append(f"%{name}%")
    if not (artist_id or name):
        return page_not_found(404)

    query = query[:-4] + ";"  # Supprimer le dernier 'AND'
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()
    conn.close()
    return jsonify(results)

# Gestion 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Ressource non trouvée.</p>", 404

# Lancement de l'app
if __name__ == '__main__':
    app.run()
