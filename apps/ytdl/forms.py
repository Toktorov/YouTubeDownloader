from django import forms
from apps.ytdl.tasks import send_feedback_email_task


class MailForm(forms.Form):
    url = forms.CharField(
        label="URL", widget=forms.Textarea(attrs={"rows": 1})
    )
    email = forms.EmailField(label="Email Address")
  
    def send_email(self):
        send_feedback_email_task.apply_async(args=[
            self.cleaned_data["url"], self.cleaned_data["email"]
            ]
        )