from flask import Flask, render_template, jsonify, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from random import sample
from util import numToStr, Const
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_get_poke')
def get_pokes():
    rands = sample(range(1, Const.NUM_POKE), 2)
    return jsonify(p_id1 = rands[0], p_id2 = rands[1])

@app.route('/_choose_winner')
def choose_winner():
    winnerstr = request.args.get('winner', none, type=str)
    rpoke_lbl = request.args.get('rpoke', none, type=str)
    lpoke_lbl = request.args.get('lpoke', none, type=str)
    if winnerstr and rpoke_lbl and lpoke_lbl:
        def clean_lbl(lbl):
            return int(lbl[1:].split(' ')[0])
        pokes = (clean_lbl(lpoke_lbl), clean_lbl(rpoke_lbl))
        if winnerstr == "#lpoke":
            winner = 0
        elif winnerstr == "#rpoke":
            winner = 1
    return render_template('index.html')

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    rating = db.Column(db.Integer)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke1_id = db.Column(db.Integer, foreign_key=True)
    poke2_id = db.Column(db.Integer, foreign_key=True)

if __name__ == '__main__':
    app.run(debug=True)
