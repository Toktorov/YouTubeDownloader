from rest_framework import serializers
from apps.ytdl.tasks import send_feedback_email_task


#Создаем сериализатор для получения данных через API
class MailSerializer(serializers.Serializer):
    url = serializers.CharField(
        label="URL"
    )
    email = serializers.EmailField(label="Email Address")

    def send_email(self): #Вызываем task
        send_feedback_email_task.delay(
            self.initial_data['url'],
            self.initial_data['email']
        )