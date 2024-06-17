from rest_framework import routers
from django.urls import path, include
from .views import FicheAgentView, DefaultDataListView, RecuCaisseView, JournalCaisseView, RecuFraisView, TimeSlotView

urlpatterns = [
    path('fiche-agent', FicheAgentView.as_view()),
    path('default-list', DefaultDataListView.as_view()),
    path('recu-caisse', RecuCaisseView.as_view()),
    path('operations-caisse', JournalCaisseView.as_view()),
    path('recu-frais', RecuFraisView.as_view()),
    path('timetable', TimeSlotView.as_view())
]