from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

@shared_task() #Создаем task для скачивая файла и отправки
def send_feedback_email_task(url, email): #Создаем функцию send_feedback_email_task, которая в параметрах принимает url, email
    video_info = YoutubeDL().extract_info(url = url,download=False) #С помощью yotube dl получаем информацию о видео в ютубе
    filename = f"{video_info['title']}.mp3" #Создаем переменную для названия файла
    options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl': f'media/{filename}',
    } #Создаем словарь с конфигурациями файла
    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']]) #Скачиваем сам файл
    mail = EmailMessage("Ваш файл готов", "Вам пришло это сообщение, потому что вы указали свой gmail в нашем сайте", settings.EMAIL_HOST_USER, [email]) #Пишем email
    mail.attach_file(f'media/{filename}') #Прикрепляем файл
    mail.send() #Отправляем файл