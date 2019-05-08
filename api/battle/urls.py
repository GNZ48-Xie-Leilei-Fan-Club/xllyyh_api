from django.urls import path

from api.battle.views.datav import IndividualView, GroupView

urlpatterns = [
    path('individual/', IndividualView.as_view()),
    path('group/', GroupView.as_view()),
]
