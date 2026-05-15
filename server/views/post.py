from flask import Blueprint, request, jsonify
from extensions import db
from models import Post, User, Comment

post_bp = Blueprint("post_bp", __name__)


# ==================== POSTS CRUD ====================

@post_bp.route("/posts", methods=["GET"])
def fetch_posts():
    posts = Post.query.all()

    results = []

    for post in posts:
        results.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id
        })

    return jsonify(results), 200


@post_bp.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()

    user = User.query.get(data["user_id"])

    if not user:
        return jsonify({"error": "User does not exist"}), 404

    new_post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"]
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({"success": "Post created successfully"}), 201


@post_bp.route("/posts/<int:post_id>", methods=["GET"])
def fetch_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    result = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "user_id": post.user_id
    }

    return jsonify(result), 200


@post_bp.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    data = request.get_json()

    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)

    db.session.commit()

    return jsonify({"success": "Post updated successfully"}), 200


@post_bp.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"success": "Post deleted successfully"}), 200


# ==================== USERS CRUD ====================

@post_bp.route("/users", methods=["GET"])
def fetch_users():
    users = User.query.all()

    results = []

    for user in users:
        results.append({
            "id": user.id,
            "username": user.username
        })

    return jsonify(results), 200


@post_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    new_user = User(
        username=data["username"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": "User created successfully"}), 201


@post_bp.route("/users/<int:user_id>", methods=["GET"])
def fetch_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User does not exist"}), 404

    result = {
        "id": user.id,
        "username": user.username
    }

    return jsonify(result), 200


@post_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User does not exist"}), 404

    data = request.get_json()

    user.username = data.get("username", user.username)

    db.session.commit()

    return jsonify({"success": "User updated successfully"}), 200


@post_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User does not exist"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"success": "User deleted successfully"}), 200


# ==================== COMMENTS CRUD ====================

@post_bp.route("/comments", methods=["GET"])
def fetch_comments():
    comments = Comment.query.all()

    results = []

    for comment in comments:
        results.append({
            "id": comment.id,
            "message": comment.message,
            "post_id": comment.post_id
        })

    return jsonify(results), 200


@post_bp.route("/comments", methods=["POST"])
def add_comment():
    data = request.get_json()

    post = Post.query.get(data["post_id"])

    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    new_comment = Comment(
        message=data["message"],
        post_id=data["post_id"]
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"success": "Comment created successfully"}), 201


@post_bp.route("/comments/<int:comment_id>", methods=["GET"])
def fetch_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    result = {
        "id": comment.id,
        "message": comment.message,
        "post_id": comment.post_id
    }

    return jsonify(result), 200


@post_bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    data = request.get_json()

    if "post_id" in data:
        post = Post.query.get(data["post_id"])

        if not post:
            return jsonify({"error": "Post does not exist"}), 404

        comment.post_id = data["post_id"]

    comment.message = data.get("message", comment.message)

    db.session.commit()

    return jsonify({"success": "Comment updated successfully"}), 200


@post_bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"success": "Comment deleted successfully"}), 200