from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

class POST(BaseModel):
    title: str
    content: str
    
app  = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}


# @app.post("/posts")
# The Body parameter is used to define the request body, in this case it is a dictionary, the ... is used to specify that the body is required
# def post(payload: dict = Body(...)):
#     return {"title": payload["title"]}


# using pydantic validation instead of manually retrieving the req body

@app.post("/posts")
def post(new_post: POST):
    print(new_post)
    return {"The title is": new_post.title} 