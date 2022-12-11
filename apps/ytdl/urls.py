from django.urls import path
from apps.ytdl.views import MailAPI


urlpatterns = [ 
    path('', MailAPI.as_view(), name = "index")
]