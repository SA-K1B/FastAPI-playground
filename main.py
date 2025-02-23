from fastapi import FastAPI
from fastapi import Body
app  = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}
@app.post("/posts")
# The Body parameter is used to define the request body, in this case it is a dictionary, the ... is used to specify that the body is required
def post(payload: dict = Body(...)):
    return {"message": "Post created"}