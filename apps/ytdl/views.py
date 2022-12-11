from django.shortcuts import render, redirect
from django.core.mail import send_mail
from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from apps.ytdl.forms import MailForm

# Create your views here.
class MailFormView(FormView):
    template_name = "index.html"
    form_class = MailForm
    success_url = "/thanks/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

def thank_you(request):
    return render(request, 'thanks.html')

def error(request):
    return render(request, 'error.html')