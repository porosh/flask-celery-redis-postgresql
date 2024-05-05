from celery import Celery
from time import sleep
from database import insert_task, get_task, get_all_tasks, update_task, delete_task


app = Celery('tasks', broker='redis://host.docker.internal:6379/0')

@app.task
def long_task():
    # Simulating a long-running task
    sleep(10)
    return 'Long task completed'

@app.task
def short_task():
    # Simulating a short-running task
    insert_task('Short task added')
    return 'Short task added to database'

@app.task
def retrieve_task(task_id):
    task = get_task(task_id)
    if task:
        return task
    else:
        return 'Task not found'

@app.task
def retrieve_all_tasks():
    tasks = get_all_tasks()
    return tasks

@app.task
def update_task_name(task_id, new_name):
    update_task(task_id, new_name)
    return 'Task updated successfully'

@app.task
def delete_task_by_id(task_id):
    delete_task(task_id)
    return 'Task deleted successfully'
