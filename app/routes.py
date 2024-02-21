from app import app, Task, Task_up, Tasks

@app.get("/")
def get_root():
    return {"Tasks_API": "Welcome"}

@app.post("/tasks/{task_id}")
def create_task(task_id: int, task: Task):
    if task_id in Tasks:
        return {"Error": "Task already exists"}
    Tasks[task_id] = task
    return task

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    if task_id in Tasks:
        return Tasks[task_id]
    return {"Error": "Not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task_up):
    if task_id not in Tasks:
        return {"Error": "Not found"}

    if task.id is not None:
        Tasks[task_id]["id"] = task.id
    if task.title is not None:
        Tasks[task_id]["title"] = task.title
    if task.Description is not None:
        Tasks[task_id]["Description"] = task.Description

    return Tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in Tasks:
        return {"Error": "Not found"}
    
    del Tasks[task_id]
    return {"Message": "Task deleted successfully"}