from fastapi import HTTPException
from app import app, Task, Task_up, Tasks

@app.get("/")
def get_root():
    return {"Tasks_API": "Welcome"}

#curl -X POST -H "Content-Type: application/json" -d "{\"id\": 3, \"title\": \"Task_3\", \"Description\": \"Task_3 things\"}" http://127.0.0.1:8000/tasks/3
@app.post("/tasks/{task_id}", response_model=Task)
async def create_task(task: Task):
    task_id = max(Tasks.keys()) + 1
    task_dict = task.dict()
    task_dict["id"] = task_id
    Tasks[task_id] = task_dict
    return task_dict

#curl http://127.0.0.1:8000/tasks/1
@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return Tasks[task_id]

#curl http://127.0.0.1:8000/tasks
@app.get("/tasks", response_model=list[Task])
async def read_tasks():
    return list(Tasks.values())

#curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Updated_Task_1\"}" http://127.0.0.1:8000/tasks/1
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_up: Task_up):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task_dict = Tasks[task_id]
    update_data = task_up.dict(exclude_unset=True)

    for field, value in update_data.items():
        task_dict[field] = value

    return task_dict

#curl -X DELETE http://127.0.0.1:8000/tasks/2
@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = Tasks.pop(task_id)
    return deleted_task