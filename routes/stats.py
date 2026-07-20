from flask import Blueprint, render_template

bp = Blueprint("stats", __name__)

@bp.route("/stats")
def index():
    return render_template("stats.html")