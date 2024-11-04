# app.py

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from models import db, User, List, Task
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))


@app.route("/")
@login_required
def index():
    """Home page showing user's lists."""
    lists = List.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", lists=lists)


@app.route("/login", methods=["GET", "POST"])
def login():
    """User login page."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """User registration page."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash("Username already exists.")
            return redirect(url_for("register"))
        # Create new user
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/logout")
@login_required
def logout():
    """User logout."""
    logout_user()
    return redirect(url_for("login"))


@app.route("/add_list", methods=["GET", "POST"])
@login_required
def add_list():
    """Add a new list."""
    if request.method == "POST":
        name = request.form["name"]
        new_list = List(name=name, user_id=current_user.id)
        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_list.html")


@app.route("/list/<int:list_id>")
@login_required
def list_view(list_id):
    """View tasks in a list."""
    todo_list = List.query.filter_by(id=list_id, user_id=current_user.id).first_or_404()
    tasks = Task.query.filter_by(list_id=list_id, parent_id=None).all()
    return render_template("list_view.html", todo_list=todo_list, tasks=tasks)


# app.py


@app.route("/add_task/<int:list_id>", methods=["GET", "POST"])
@app.route("/add_task/<int:list_id>/<int:parent_id>", methods=["GET", "POST"])
@login_required
def add_task(list_id, parent_id=None):
    """Add a new task or subtask."""
    if request.method == "POST":
        description = request.form["description"]

        # Check if level is valid; if not, default to 1
        level_str = request.form.get("level", "1")
        level = int(level_str) if level_str.isdigit() else 1

        if level > 3:
            flash("Maximum depth reached.")
            return redirect(url_for("list_view", list_id=list_id))

        new_task = Task(description=description, list_id=list_id, parent_id=parent_id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("list_view", list_id=list_id))

    # Pass the level variable as needed in the template
    return render_template("add_task.html", list_id=list_id, parent_id=parent_id)


@app.route("/complete_task/<int:task_id>")
@login_required
def complete_task(task_id):
    """Mark a task as complete."""
    task = Task.query.get_or_404(task_id)
    if task.list.user_id != current_user.id:
        flash("Unauthorized action.")
        return redirect(url_for("index"))
    task.completed = True
    db.session.commit()
    return redirect(url_for("list_view", list_id=task.list_id))


@app.route("/toggle_collapse/<int:task_id>")
@login_required
def toggle_collapse(task_id):
    """Toggle collapse state of a task."""
    task = Task.query.get_or_404(task_id)
    if task.list.user_id != current_user.id:
        flash("Unauthorized action.")
        return redirect(url_for("index"))
    task.collapsed = not task.collapsed
    db.session.commit()
    return redirect(url_for("list_view", list_id=task.list_id))


@app.route("/move_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def move_task(task_id):
    """Move a task to a different list."""
    task = Task.query.get_or_404(task_id)
    if task.list.user_id != current_user.id:
        flash("Unauthorized action.")
        return redirect(url_for("index"))
    if request.method == "POST":
        new_list_id = int(request.form["new_list_id"])
        task.list_id = new_list_id
        db.session.commit()
        return redirect(url_for("list_view", list_id=new_list_id))
    lists = List.query.filter_by(user_id=current_user.id).all()
    return render_template("move_task.html", task=task, lists=lists)


@app.route("/delete_list/<int:list_id>", methods=["POST"])
@login_required
def delete_list(list_id):
    """Delete a list and all its associated tasks."""
    todo_list = List.query.filter_by(id=list_id, user_id=current_user.id).first()
    if todo_list is None:
        flash("List not found or you don't have permission to delete this list.")
        return redirect(url_for("index"))

    # Delete all tasks associated with the list
    Task.query.filter_by(list_id=list_id).delete()
    # Delete the list itself
    db.session.delete(todo_list)
    db.session.commit()

    flash("List and all its tasks have been deleted.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
