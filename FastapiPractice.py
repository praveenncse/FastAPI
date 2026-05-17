from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def print_msg():
    return {'Message':'Hello Praveen !!'}