if _name_ == "_main_":
    import uvicorn
    uvicorn.run(prediction_app, host="0.0.0.0", port=8000)
