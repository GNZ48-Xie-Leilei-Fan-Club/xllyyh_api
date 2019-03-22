from django.urls import path

from api.chatbot.views.keyworded_response import KeywordedResponseList, IgnoreNumberList

urlpatterns = [
    path('keyworded_responses/', KeywordedResponseList.as_view()),
    path('ignore_numbers/', IgnoreNumberList.as_view())
]
