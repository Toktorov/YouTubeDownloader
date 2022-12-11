from django.conf import settings
from django.core.mail import EmailMessage

from downloader.celery import app


# @app.task