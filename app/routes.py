from fastapi import HTTPException, Request
import redis
import json
from app import app, Task, Task_up

def get_client_ip(request: Request):
    return request.client.host

r = redis.Redis(
    host='redis',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

@app.get("/")
def get_root():
    return {"Tasks_API": "Welcome"}

#curl -X POST -H "Content-Type: application/json" -d "{\"id\": 1,\"title\": \"Task_1\", \"Description\": \"Task_1 things\"}" http://127.0.0.1:8000
@app.post("/tasks/{task_id}", response_model=Task)
async def create_task(request: Request, task: Task):
    ip = get_client_ip(request)
    
    tasks_str = r.get(ip)
    tasks = json.loads(tasks_str) if tasks_str else {}
    
    task_id = max(tasks.keys(), default=0) + 1
    task_dict = task.dict()
    task_dict["id"] = task_id
    tasks[task_id] = task_dict
    
    r.set(ip, json.dumps(tasks))
    
    return task_dict

#curl http://127.0.0.1:8000/tasks/1
@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(request: Request, task_id: str):
    ip = get_client_ip(request)
    
    tasks_str = r.get(ip)
    
    if not tasks_str:
        raise HTTPException(status_code=404, detail="No tasks found for the IP")

    tasks = json.loads(tasks_str)
    
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return tasks[task_id]

#curl http://127.0.0.1:8000/tasks
@app.get("/tasks", response_model=list[Task])
async def read_tasks(request: Request):
    ip = get_client_ip(request)
    
    tasks_str = r.get(ip)
    tasks = json.loads(tasks_str) if tasks_str else {}
    
    return list(tasks.values())

#curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Updated_Task_1\"}" http://127.0.0.1:8000/tasks/1
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(request: Request, task_id: str, task_up: Task_up):
    ip = get_client_ip(request)
    
    tasks_str = r.get(ip)
    
    if not tasks_str:
        raise HTTPException(status_code=404, detail="No tasks found for the IP")

    tasks = json.loads(tasks_str)
    
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task_dict = tasks[task_id]
    update_data = task_up.dict(exclude_unset=True)

    for field, value in update_data.items():
        task_dict[field] = value

    r.set(ip, json.dumps(tasks))
    
    return task_dict

#curl -X DELETE http://127.0.0.1:8000/tasks/2
@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(request: Request, task_id: str):
    ip = get_client_ip(request)
    
    tasks_str = r.get(ip)
    
    if not tasks_str:
        raise HTTPException(status_code=404, detail="No tasks found for the IP")

    tasks = json.loads(tasks_str)
    
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_id)

    r.set(ip, json.dumps(tasks))
    
    return deleted_task