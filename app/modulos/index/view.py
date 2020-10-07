from flask import Blueprint, render_template, url_for 

main = Blueprint("main", __name__)

@main.route("/")
def homepage():
  return render_template('index.html')

@main.route('/')
def info():
  return render_template('info.html')
