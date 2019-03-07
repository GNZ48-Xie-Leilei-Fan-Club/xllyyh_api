from rest_framework import generics
from rest_framework.response import Response

from api.models.keyworded_response import KeywordedResponse
from api.serializers.keyworded_response import KeywordedResponseSerializer

class KeywordedResponseList(generics.ListAPIView):
    serializer_class = KeywordedResponseSerializer
    
    def get_queryset(self):
        return KeywordedResponse.objects.all()
