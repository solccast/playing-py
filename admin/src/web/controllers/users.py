from flask import Blueprint, render_template

bp = Blueprint("usuarios", __name__, url_prefix="/users")

@bp.route("/")
def inicio():
    return render_template("layout.html")

@bp.route("/1")
def acceso_uno():
    return ("Hola!, esto no es un html")