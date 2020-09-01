from django.urls import path
from .views import TournamentListings, TournamentDetail

urlpatterns = [
    path('', TournamentListings.as_view(), name="tournaments_listing"),
    path('<str:slug>/', TournamentDetail.as_view(), name="tournament_detail"),
]