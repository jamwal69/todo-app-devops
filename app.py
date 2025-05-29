from flask import Flask, request, jsonify, render_template_string, redirect, url_for

app = Flask(__name__)
tasks = []

# HTML template
HTML_PAGE = '''
<!doctype html>
<html>
<head><title>ToDo App</title></head>
<body>
    <h1>My ToDo List</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ loop.index0 }}. {{ task }} 
                <a href="/delete/{{ loop.index0 }}">[Delete]</a>
            </li>
        {% endfor %}
    </ul>

    <form method="POST" action="/add">
        <input name="task" placeholder="Enter a task" required />
        <button type="submit">Add Task</button>
    </form>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task_web():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

@app.route("/delete/<int:index>")
def delete_task_web(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('home'))

# API: GET all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# API: Add task via JSON
@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks.append(task)
    return jsonify({"message": "Task added"}), 201

# API: Delete task via index
@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Invalid index"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
