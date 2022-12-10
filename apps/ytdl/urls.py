from django.urls import path
from apps.ytdl.views import index, thank_you, error


urlpatterns = [
    path('', index, name = "index"),
    path('thanks/', thank_you, name = "thank_you"),
    path('error/', error, name = "error")
]