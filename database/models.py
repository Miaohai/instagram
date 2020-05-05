from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Profile(db.Document):
    username = db.StringField(required=True,unique=True)
    num_follower = db.IntField(required=True)
    num_followee = db.IntField(required=True)
    num_posts = db.IntField(required=True)
    profile_pic = db.StringField(required=True)
    biography = db.StringField(required=True)
    is_business_account = db.BooleanField(required=True)
    posts = db.ListField(required=True)