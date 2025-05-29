import app

def test_add_task():
    app.tasks.clear()
    app.tasks.append("Test task")
    assert "Test task" in app.tasks

def test_delete_task():
    app.tasks.clear()
    app.tasks.append("Delete me")
    app.tasks.pop(0)
    assert "Delete me" not in app.tasks
