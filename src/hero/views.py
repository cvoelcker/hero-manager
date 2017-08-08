from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Group
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string


# Create your views here.

class HomeView(TemplateView):
    template_name = "base.html"


class GroupView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('result')


@login_required
def index(request):
    return HttpResponse("Hello World. You are at the hero index")


@login_required
def diaries_list(request):
    pass


@login_required
def profile(request):
    pass


def groups_list(request):
    master_groups = Group.objects.filter(game_master=request.user)
    return HTTPResponse(template.render(request, 'groups_base.html', {}))
