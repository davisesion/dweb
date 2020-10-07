from flask import Blueprint, render_template

cons = Blueprint("cons", __name__)

@cons.route("/consulta")
def conspage():
  return render_template('consulta.html')
