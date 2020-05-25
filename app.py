import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', '')
db = SQLAlchemy(app)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_1 = db.Column(db.String)
    score_1 = db.Column(db.Integer)
    player_2 = db.Column(db.String)
    score_2 = db.Column(db.Integer)

db.create_all()


@app.route('/')
def index():
    scores = Score.query.all()
    return render_template('index.html', scores=scores)
