from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str


@app.get("/message")
async def print_msg():
    return {'Message':'Hello Praveen !!'}

@app.post('/posts')
def posts(payload: Post):
    print(payload)
    return {'data':payload}
  


@app.post('/createpost')
def createpost():
    return {'message':'created post'}