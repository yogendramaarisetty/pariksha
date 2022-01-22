from celery import shared_task
from celery import shared_task
from celery_progress.backend import ProgressRecorder
import time

@shared_task(bind=True)
def add(x,y):
    return x+y



@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def my_task(self, seconds):
    progress_recorder = ProgressRecorder(self)
    result = 0
    for i in range(seconds):
        time.sleep(1)
        result += i
        progress_recorder.set_progress(i + 1, seconds, description='my progress description')
    return result