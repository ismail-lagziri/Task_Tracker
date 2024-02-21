# app/main.py
from app.routes import app
from fastapi_redis_rate_limiter import RedisRateLimiterMiddleware, RedisClient

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)