from django.shortcuts import render, redirect
from django.core.mail import send_mail
from youtube_dl import YoutubeDL

# Create your views here.
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        email = request.POST.get('email')
        if url and email:
            try:
                video_info = YoutubeDL().extract_info(url = url,download=False)
                filename = f"{video_info['title']}.mp3"
                options={
                    'format':'bestaudio/best',
                    'keepvideo':False,
                    'outtmpl': f'media/{filename}',
                }
                with YoutubeDL(options) as ydl:
                    ydl.download([video_info['webpage_url']])
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