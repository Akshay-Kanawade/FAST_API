from fastapi import FastAPI
from . import schemas
from . import models
from .database import Engine



app = FastAPI()

models.Base.metadata.create_all(Engine)




@app.post("/blog")
async def blog_post(title, body):
    
    return f"blog posted    title - {title}  ***** body - {body}"



@app.post("/post_blog")
async def blog_post(blog:schemas.BLOG):
    
    return f"blog model posted    title - {blog.title}  ***** body - {blog.body}"