import os
from fastapi import BackgroundTasks

def remove_file_later(path: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(os.remove, path)
