from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopproduct.settings")

app = Celery("shopproduct")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


def shared_task():
    return None
