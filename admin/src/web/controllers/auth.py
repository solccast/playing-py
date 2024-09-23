from flask import Blueprint, request, jsonify, render_template
from flask import redirect, url_for, flash, session
from src.core import auth

bp = Blueprint("auth", __name__, url_prefix="/acceso")


@bp.get("/")
def login():
    """
    Envia el formulario
    """
    return render_template("auth/login.html")


@bp.post("/")
def authenticate():
    """
    Recibe la data del login
    """
    params = request.form #se obtenemos los parametros en cada request
    
    user = auth.find_user_by_email_and_password(params["email"], params["password"])

    if not user:
        flash("Usuario o contraseña incorrecta", "error")

        return redirect(url_for("auth.login"))

    session["user"] = user.email
    flash("Bienvenido, la sesión se inició correctamente", "success")    
    
    return redirect(url_for("usuarios.inicio"))


@bp.get("/logout")
def logout():
    pass

