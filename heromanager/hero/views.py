from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero

# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at the hero index")

def hero_list(request):
    response = "These heros are registered:"
    for hero in Hero.objects.all():
        response += "<p> {} -- {}</p>".format(hero, hero.player)
    return HttpResponse(response)
