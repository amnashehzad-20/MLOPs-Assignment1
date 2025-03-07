from flask import Flask, render_template, request, redirect, url_for
from database import db, Task  # Updated reference

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# ======================== ADD TASK ==========================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

# ========================  COMPLETE TASK ==========================
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed  # Toggle completion
        db.session.commit()
    return redirect(url_for("index"))

# ======================== DELETE TASK ==========================
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))

# ========================RUN FLASK APP ==========================
if __name__ == "__main__":
    app.run(debug=True)
