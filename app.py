from flask import Flask
from routes.home import bp as home_bp
from routes.stats import bp as stats_bp
from routes.nova_rotina import bp as nova_rotina_bp
from routes.auth import bp as auth_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(stats_bp)
app.register_blueprint(nova_rotina_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)