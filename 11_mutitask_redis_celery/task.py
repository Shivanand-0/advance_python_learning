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
def process_file(file_name):
    print("processing file: ", file_name)
    time.sleep(5)
    return f"{file_name} completed."

