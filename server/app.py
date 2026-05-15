from flask import Flask
from flask_cors import CORS
from extensions import db, migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "sehtrsdyhndtejdydunuyehbdrvteryhe"

CORS(app)

db.init_app(app)
migrate.init_app(app, db)

import models

from views.post import post_bp
app.register_blueprint(post_bp)


@app.route("/")
def home():
    return {
        "message": "Flask app is running",
        "routes": [str(rule) for rule in app.url_map.iter_rules()]
    }


if __name__ == "__main__":
    app.run(port=5000, debug=True)