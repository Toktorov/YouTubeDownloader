from apps.ytdl.serializers import MailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.ytdl.tasks import send_feedback_email_task

# Create your views here.
class MailAPI(GenericAPIView):
    serializer_class = MailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        serializer.send_email()
        return Response({'success': 'Успешно отправлено'}, status=status.HTTP_200_OK)