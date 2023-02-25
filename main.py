from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/')
def Blogs():
    return "Get all blogs"

@app.get('/blog/{id}')
def Blog_id(id:int):
    return f"Get blog by id -  {id}"

@app.get('/blog/{id}/comments')
def Blog_Comments_by_Id(id:str):
    return f"Get blog comments by id - {id}"



class BLOG(BaseModel):
    title : str
    id:int
    desc : str

@app.post("/blog")
def BLog(blog: BLOG):
    return f"blog posted {blog}"

 
# if __name__ == "__main__" :
#     uvicorn.run(app)