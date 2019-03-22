from rest_framework import generics
from rest_framework.response import Response

from api.chatbot.models.keyworded_response import KeywordedResponse, IgnoreNumber
from api.chatbot.serializers.keyworded_response import KeywordedResponseSerializer, IgnoreNumberSerializer

class KeywordedResponseList(generics.ListAPIView):
    serializer_class = KeywordedResponseSerializer
    
    def get_queryset(self):
        return KeywordedResponse.objects.all()


class IgnoreNumberList(generics.ListAPIView):
    serializer_class = IgnoreNumberSerializer

    def get_queryset(self):
        return IgnoreNumber.objects.all()
