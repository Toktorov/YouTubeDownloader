import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "downloader.settings")
app = Celery("downloader")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()