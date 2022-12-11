import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "downloader_rest.settings")
app = Celery("downloader_rest")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()