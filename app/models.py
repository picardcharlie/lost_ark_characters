from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    uid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    user_character = db.relationship("Character", backref = "user", lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You can't call the password you rat")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash


class Character(db.Model):
    __tablename__ = "characters"
    charid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    character_name = db.Column(db.String(25))
    character_gs = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.uid"))

    daily_chaos = db.Column(db.Integer)

    def __init__(self, character_name, character_gs, daily_chaos):
        self.character_name = character_name
        self.character_gs = character_gs
        self.daily_chaos = daily_chaos