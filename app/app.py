from flask import Flask, render_template, request, redirect, url_for
from database import db, Task  # Ensure database.py defines db & Task properly

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
with app.app_context():
    db.init_app(app)
    db.create_all()


# ========================  ADD TASK ==========================

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            try:
                new_task = Task(title=title)
                db.session.add(new_task)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(f"Error adding task: {e}")  # Debugging log

    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


# ======================== RUN FLASK APP ==========================

if __name__ == "__main__":
    app.run(debug=True)
