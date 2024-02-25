from fastapi.responses import JSONResponse
from fastapi_redis_rate_limiter import RedisRateLimiterMiddleware, RedisClient
from fastapi.middleware.cors import CORSMiddleware
from app.utils import send_notification
from app.routes import app as task_app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import requests

redis_client = RedisClient(host="redis", port=6379, db=0)

task_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

task_app.add_middleware(RedisRateLimiterMiddleware, redis_client=redis_client, limit=10, window=30)

@task_app.get("/heartbeat")
async def heartbeat():
    return JSONResponse(content={"status": "ok", "timestamp": str(datetime.datetime.now())})

def check_heartbeat():
    response = requests.get("http://localhost:8000/heartbeat")
    if response.status_code != 200:
        send_notification()

scheduler = BackgroundScheduler()
scheduler.add_job(lambda: print("Heartbeat"), 'interval', minutes=10)
scheduler.add_job(check_heartbeat, 'interval', minutes=10)
scheduler.start()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(task_app, host="0.0.0.0", port=8000)