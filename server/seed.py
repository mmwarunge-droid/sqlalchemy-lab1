from faker import Faker

from app import app
from extensions import db
from models import Comment, Post, User

fake = Faker()

with app.app_context():
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()

    users = [
        User(username=fake.unique.user_name())
        for _ in range(3)
    ]

    db.session.add_all(users)
    db.session.flush()

    posts = []

    for index in range(9):
        post = Post(
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=5),
            user_id=users[index % len(users)].id
        )

        posts.append(post)

    db.session.add_all(posts)
    db.session.flush()

    comments = []

    for post in posts:
        comment = Comment(
            message=fake.sentence(nb_words=12),
            post_id=post.id
        )

        comments.append(comment)

    db.session.add_all(comments)
    db.session.commit()

    print("Database seeded successfully.")
    print("Created 3 users, 9 posts, and 9 comments.")