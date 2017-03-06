"""
    File name: app.py
    Author: Srinivasa Manda
    Python Version: 2.7
"""
from flask import Flask, render_template, redirect, request,json
import sqlite3

app = Flask(__name__)


@app.route('/')
def appointments():
    return render_template("index.html")


@app.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        date = request.form['inputdate']
        time = request.form['inputtime']
        description = request.form['inputdescription']

        with sqlite3.connect('appointments.db') as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO APP (date,time,description) VALUES(?,?,?) ",
                [date, time, description])
            con.commit()
            return redirect('/')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        try:
            search_string = request.form['search-id']
            print search_string
            conn = sqlite3.connect("appointments.db")
            cur = conn.cursor()

            cur.execute("select * from app where description like ? "
                        "", ('%' + str(search_string) + '%',))
            app_records = cur.fetchall()
            app_list = []
            for record in app_records:
                items_dict = {
                    'date': record[0],
                    'time': record[1],
                    'description': record[2]}
                app_list.append(items_dict)

            return json.dumps(app_list)

        except Exception as e:
            return json.dumps({'error': e})

if __name__ == "__main__":
    app.run(debug=True)
