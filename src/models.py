import enum
from sqlalchemy import Enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firtsname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)



class Follower(db.Model):
    __tablename__= "Follower"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("User.id"))


class Media(db.Model):
    __tablename__= "Media"

    id: Mapped[int] = mapped_column(primary_key=True)
    #type: Mapped[enum] = mapped_column(primary_key=False)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))


class Post(db.Model):
    __tablename__= "Post"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

class Comment(db.Model):
    __tablename__= "Comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))



    
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
