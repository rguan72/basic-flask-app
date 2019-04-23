from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def first():
    return render_template("app.html")

@app.route('/receive_json', methods=['POST'])
def receive_json():
    print("The request is being sent to: ", request.url)
    req_json = request.get_json()
    x = req_json['content']
    print("The data in the input box is: ", x)

    with sqlite3.connect('example.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS data (hi)')
        cur.execute('INSERT INTO data (hi) VALUES (?)', (x,))
        conn.commit()

    # jsonify can also take in a dict or list
    return jsonify(data=x, method="json_sent")

@app.route('/input', methods=['POST'])
def receive_form():
    print("The request is being sent to: ", request.url)
    x = request.form['valform']
    print("The data in the input box is: ", x)

    with sqlite3.connect('example.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS data (hi)')
        cur.execute('INSERT INTO data (hi) VALUES (?)', (x,))
        conn.commit()

    return ('', 204)
