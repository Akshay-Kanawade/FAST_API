# background tasks to be run after returning a response.


# Email notifications sent after performing an action


# The class BackgroundTasks comes directly from starlette.background
# By only using BackgroundTasks (and not BackgroundTask), it's then possible 
# to use it as a path operation function parameter and have FastAPI handle
# the rest for you, just like when using the Request object directly.

# f you need to perform heavy background computation and you don't
# necessarily need it to be run by the same process (for example,
# you don't need to share memory, variables, etc), you might benefit
# from using other bigger tools like Celery.

# They tend to require more complex configurations, a message/job queue 
# manager, like RabbitMQ or Redis, but they allow you to run background 
# tasks in multiple processes, and especially, in multiple servers.

from fastapi import BackgroundTasks, FastAPI
from typing import Union
app =FastAPI()


def write_notification(email: str, message: Union[str, None] = None ):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for Email : --------{email} \
                    message : ---------- {message}"
        email_file.write(content)
        
        
@app.post('/notification/{email}')
async def send_notification(email:str, message:str, background_tasks: BackgroundTasks ):
    background_tasks.add_task(write_notification, email, message=message)
    return {"message": "Notification write in the background"}
     

