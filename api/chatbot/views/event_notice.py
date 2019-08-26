from rest_framework import generics
from rest_framework.response import Response

from api.models.event_notice import NewMemberNotice
from api.chatbot.serializers.event_notice import NewMemberNoticeSerializer

class NewMemberNoticeList(generics.ListAPIView):
    serializer_class = NewMemberNoticeSerializer
    
    def get_queryset(self):
        return NewMemberNotice.objects.all()