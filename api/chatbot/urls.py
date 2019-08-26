from django.urls import path

from api.chatbot.views.keyworded_response import KeywordedResponseList, IgnoreNumberList
from api.chatbot.views.event_notice import NewMemberNoticeList

urlpatterns = [
    path('keyworded_responses/', KeywordedResponseList.as_view()),
    path('ignore_numbers/', IgnoreNumberList.as_view()),
    path('new_member_notices/', NewMemberNoticeList.as_view()),
]
