from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # Store tasks in memory

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            task_id = len(tasks) + 1
            tasks.append({"id": task_id, "title": title, "completed": False})
    return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["completed"] = not task["completed"]
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
