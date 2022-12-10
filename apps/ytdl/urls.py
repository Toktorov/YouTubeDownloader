from django.urls import path
from apps.ytdl.views import index


urlpatterns = [
    path('', index, name = "index")
]