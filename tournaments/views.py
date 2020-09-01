from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tournament

class TournamentListings(ListView):
    model = Tournament
    template_name = 'tournaments/tournament_list.html'
    

class TournamentDetail(DetailView):
    model = Tournament
    template_name = 'tournaments/tournament_detail.html'
    
