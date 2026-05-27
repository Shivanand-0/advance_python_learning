# code of celery
from celery import Celery
import time

#create celery app
app=Celery(
    "tasks",
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Define task
@app.task
def add(x,y):
    time.sleep(6)
    return x+y

