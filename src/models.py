from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False) # JOIN SQL

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email
        }

    def serialize_with_profile(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "profile": self.profile.serialize()
        }

        """
        {
            "id": 1,
            "name": "",
            "lastname": "",
            "email": "",
            "profile": {
                "id": 1,
                "bio": "",
                "twitter": "",
                "facebook": "",
                "instagram": "",
                "linkedin": ""
            }
        }
        """


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text, default="")
    twitter = db.Column(db.String(100), default="")
    facebook = db.Column(db.String(100), default="")
    instagram = db.Column(db.String(100), default="")
    linkedin = db.Column(db.String(100), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "twitter": self.twitter,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "linkedin": self.linkedin
        }

    def serialize_with_user(self):
        return {
            "id": self.id,
            "name": self.user.name + " " + self.user.lastname, 
            "bio": self.bio,
            "twitter": self.twitter,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "linkedin": self.linkedin
        }

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()