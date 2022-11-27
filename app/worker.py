# tasks.py
import os
import time
import celery

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

cel = celery.Celery(
  'tasks',
  broker=CELERY_BROKER,
  backend=CELERY_BACKEND
)
