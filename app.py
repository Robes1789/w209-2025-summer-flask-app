from flask import Flask, render_template, jsonify
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def w209():
    file = 'about9.jpg'
    return render_template('w209.html', file=file)

@app.route('/map')
def map():
    return render_template('index.html')

@app.route("/getData/<int:year>")
def getData(year):
    revenue = pd.read_csv(os.path.join(APP_FOLDER, "static/data/1_Revenues.csv"))
    if year < 1942 or year > 2008:
        return "Error in the year range"
    filteredRevenue = revenue[revenue['Year4'] == year][["Name", "Year4", "Total Revenue", "Population (000)"]]
    return filteredRevenue.to_json(orient='records')

@app.route('/api')
def api():
    return jsonify({"x": 5})

@app.route('/players/count')
def player_count():
    conn = sqlite3.connect(os.path.join(APP_FOLDER, "players_20.db"))
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run()

