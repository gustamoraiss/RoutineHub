from flask import Blueprint, render_template

bp = Blueprint("nova_rotina", __name__)

@bp.route("/rotinas/nova")
def index():
    return render_template("nova_rotina.html")