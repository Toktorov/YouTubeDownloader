from django.shortcuts import render
from django.views.generic.edit import FormView
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