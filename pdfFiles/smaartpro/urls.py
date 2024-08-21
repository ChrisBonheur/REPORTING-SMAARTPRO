from rest_framework import routers
from django.urls import path, include
from .views import FicheAgentView, DefaultDataListView, RecuCaisseView, JournalCaisseView, RecuFraisView, TimeSlotView, ClosedCashView, FicheEleveView, FicheTeacherView, BulletinView, AirtelMomo

urlpatterns = [
    path('fiche-agent', FicheAgentView.as_view()),
    path('default-list', DefaultDataListView.as_view()),
    path('bulletin', BulletinView.as_view()),
    path('recu-caisse', RecuCaisseView.as_view()),
    path('operations-caisse', JournalCaisseView.as_view()),
    path('recu-frais', RecuFraisView.as_view()),
    path('timetable', TimeSlotView.as_view()),
    path('closed-sold', ClosedCashView.as_view()),
    path('fiche-eleve', FicheEleveView.as_view()),
    path('fiche-teacher', FicheTeacherView.as_view()),
    path('airtelmoney', AirtelMomo.as_view())
]