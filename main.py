if __name__ == "__main__":
    import uvicorn
    uvicorn.run(prediction_app, host="0.0.0.0", port=8000)
