from django.urls import path
from apps.ytdl.views import MailFormView, thank_you, error


urlpatterns = [
    path('', MailFormView.as_view(), name = "index"),
    path('thanks/', thank_you, name = "thank_you"),
    path('error/', error, name = "error")
]