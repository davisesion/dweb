from flask import Flask, render_template

from config import DATABASE
from peewee import SqliteDatabase

app = Flask(__name__)

app.config.from_object('config')

db = SqliteDatabase(DATABASE)

@app.before_request
def before_request():
  db.connect()

@app.after_request
def after_request(response):
  db.close()
  return response

from app.modulos.consulta.view import cons as blueprint_consulta
app.register_blueprint(blueprint_consulta)

from app.modulos.index.view import main as blueprint_home
app.register_blueprint(blueprint_home)

from app.modulos.info.view import info as blueprint_info
app.register_blueprint(blueprint_info)
