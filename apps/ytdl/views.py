from apps.ytdl.serializers import MailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.ytdl.tasks import send_feedback_email_task

# Create your views here.
class MailAPI(APIView):
    serializer_class = MailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'success': 'Успешно отправлено'}, status=status.HTTP_200_OK)