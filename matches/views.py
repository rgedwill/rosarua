from django.shortcuts import render
from django.views.generic.list import ListView
from .models import InterpretationRequest
# Create your views here.
class Match(ListView):
    template_name = 'matches/match_finder.html'
    model = InterpretationRequest
    context_object_name = 'match_info'