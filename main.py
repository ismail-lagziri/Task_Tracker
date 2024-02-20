from app.routes import task 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(task, host="0.0.0.0", port=8000)
