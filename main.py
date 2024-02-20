if __name__ == "__main__":
    from app.routes import task 
    import uvicorn
    uvicorn.run(task, host="0.0.0.0", port=8000)
