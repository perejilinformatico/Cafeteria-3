from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cafe_sql_user:GXVyodnjpoE2kKTB3PtznYaTLDFgym0B@dpg-d37v88be5dus739np980-a/cafe_sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/cafe", methods=["GET","POST"])
def api_cafe():
    if request.method == "POST":
        data = request.get_json()
        nombre_cafe = data.get("cafe", "Desconocido")
        nuevo_cafe = Cafe(nombre=nombre_cafe)
        db.session.add(nuevo_cafe)
        db.session.commit()
    cafes = [c.nombre for c in Cafe.query.all()]
    return jsonify({"cafes_totales": cafes})

@app.route("/otra")
def otra_pagina():
    return render_template("otra.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)