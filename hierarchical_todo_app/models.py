from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """Model for user accounts."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relationship to link lists to a user
    lists = db.relationship("List", backref="user", lazy=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password_hash, password)


class List(db.Model):
    __tablename__ = "lists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Cascade delete to remove all tasks when a list is deleted
    tasks = db.relationship(
        "Task", backref="list", lazy=True, cascade="all, delete-orphan"
    )


class Task(db.Model):
    """Model for tasks."""

    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    collapsed = db.Column(db.Boolean, default=False)
    list_id = db.Column(
        db.Integer, db.ForeignKey("lists.id"), nullable=False
    )  # Correct foreign key reference
    parent_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=True)

    # Relationship to define hierarchical subtasks
    subtasks = db.relationship(
        "Task", backref=db.backref("parent", remote_side=[id]), lazy=True
    )

    def is_collapsed(self):
        """Return whether the task is collapsed."""
        return self.collapsed
