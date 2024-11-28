from django.shortcuts import render, get_object_or_404
from .models import Game
from django.views.generic import ListView, DetailView

class GameListView(ListView):
    model = Game
    template_name = 'gameapp/game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name = 'gameapp/game_detail.html'
    context_object_name = 'game'
