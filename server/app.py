from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


CORS(app)
app.secret_key = "sehtrsdyhndtejdydunuyehbdrvteryhe"


# model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


# CRUD
# READ
@app.route("/posts")
def fetch_posts():
    # fetching data in sqlalchemy
    posts = Post.query.all()
    
    results = []

    for post in posts:
        results.append({
            "id":post.id,
            "title": post.title,
            "content": post.content}
        )
    return jsonify(results), 200

# POST DATA/ADD
# READ 1
# UPDATE
# DELETE



# export FLASK_APP=app.py
# export FLASK_DEBUG=1

