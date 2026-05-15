from faker import Faker

from app import app, db
from models import Comment, Post, User

fake = Faker()

# add comments
with app.app_context():#remove all data before seeding
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()
    # create 3 users, 9 post, 9 comments
    users = [User(username=fake.unique.user_name()) for _ in range(3)]
    db.session.add_all(users) # add all users to the session
    db.session.flush() # flush to get the ids of the users
    
    # -- create 9 posts, each post is assigned to a user in a round-robin fashion
    posts = []
    for index in range(9):
        post = Post(
            title=fake.sentence(nb_words=5),  # generate a random title with 5 words    
            content=fake.paragraph(nb_sentences=5), # generate a random content with 5 sentences
            user_id=users[index % len(users)].id,# assign user_id in a round-robin fashion 
        )
        posts.append(post)
    
    db.session.add_all(posts) # add all posts to the session
    db.session.flush() # flush to get theids of the posts
    

    #-- create 9 comments, each comment is assigned to a post in a round-robin fashion
    comments = []

    for post in posts:
        comment = Comment(
            message=fake.sentence(nb_words=12),
            post_id=post.id
        )
        comments.append(comment)
    db.session.add_all(comments)
    db.session.commit() # commit all changes to the database, this will save the users, posts, and comments to the database tables all at once

    print("Database seeded successfully!")
    print("Created 3 users, 9 posts, and 9 comments.")


