from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        email = request.POST.get('email')
        if url and email:
            try:
                send_mail(
                    # title:
                    f"Cryxxen",
                    # message:
                    f"{url} {email}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
                )
                return redirect("thank_you")
            except:
                return redirect("https://github.com/Toktorov/CryxxenYouTube/blob/django/donwloader/urls.py")
        # else:
        #     return redirect()
    return render(request, 'index.html')

def thank_you(request):
    return render(request, 'thanks.html')

def error(request):
    return render(request, 'error.html')