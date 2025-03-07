from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # Store tasks in memory

# ======================== ADD TASK ==========================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})
    return render_template("index.html", tasks=tasks)

# ========================  COMPLETE TASK ==========================
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]  # Toggle completion
            break
    return redirect(url_for("index"))

# ========================RUN FLASK APP ==========================
if __name__ == "__main__":
    app.run(debug=True)
