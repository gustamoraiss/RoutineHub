from flask import Flask
from routes.home import bp as home_bp
from routes.stats import bp as estatisticas_bp
from routes.nova_rotina import bp as nova_rotina_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(estatisticas_bp)
app.register_blueprint(nova_rotina_bp)

if __name__ == "__main__":
    app.run(debug=True)