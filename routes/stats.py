from flask import Blueprint, render_template

bp = Blueprint("estatisticas", __name__)

@bp.route("/estatisticas")
def index():
    return render_template("estatisticas.html")