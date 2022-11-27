# tasks.py
import os
import time
import celery
import celeryconfig

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery(
   'tasks',
   broker=CELERY_BROKER,
   backend=CELERY_BACKEND
)
app.config_from_object(celeryconfig)


@app.task
def run():
   time.sleep(10)
   print('処理　おわた')
   return 'おわったよ'


@app.task
def calc(a, b):
   return a+b


@app.task(name='add')
def add(x, y):
   return x + y


@app.task(name='post.folder', bind=True)
def post_folder(self, name):
   #return {"result": f"post {name}"}
   return {
      "result": f"post {name}",
      "self??" : f"{self}"
      }
