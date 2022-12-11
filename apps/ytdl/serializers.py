from rest_framework import serializers
from apps.ytdl.tasks import send_feedback_email_task

class MailSerializer(serializers.Serializer):
    url = serializers.CharField(
        label="URL"
    )
    email = serializers.EmailField(label="Email Address")

    def create(self, validated_data):
        send_feedback_email_task.apply_async(args=[
            self.initial_data["url"], self.initial_data["email"]
            ]
        )
        return True