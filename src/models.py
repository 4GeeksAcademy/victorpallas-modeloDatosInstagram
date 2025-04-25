from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

db = SQLAlchemy()

class MediaType(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"

class User(db.Model):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Follower(db.Model):
    __tablename__= "Follower"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

class Post(db.Model):
    __tablename__= "Post"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

class Media(db.Model):
    __tablename__= "Media"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))

class Comment(db.Model):
    __tablename__= "Comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }
