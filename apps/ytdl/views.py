from apps.ytdl.serializers import MailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MailAPI(GenericAPIView): #Создае API  
    serializer_class = MailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.send_email()
        return Response({'success': 'Успешно отправлено'}, status=status.HTTP_200_OK)