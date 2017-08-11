from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from hero.models import Group
from hero.forms import GroupForm


# Create your views here.

class HomeView(TemplateView):
    template_name = "base.html"


class GroupView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_all.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        user = self.request.user
        context['gm_groups'] = user.gaming_group_master.all()
        context['player_groups'] = user.gaming_group.all()
        return context


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups_detail.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get(name=self.kwargs['name'])


class GroupAdminView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups_all.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        user = self.request.user
        context['gm_groups'] = user.gaming_group_master.all()
        context['player_groups'] = user.gaming_group.all()
        return context


class GroupAddView(LoginRequiredMixin, FormView):
    template_name = 'groups_add.html'
    form_class = GroupForm
    success_url = reverse_lazy('hero:group_add_success')


class GroupSuccessView(LoginRequiredMixin, TemplateView):
    pass


@login_required
def index(request):
    return HttpResponse("Hello World. You are at the hero index")


@login_required
def diaries_list(request):
    pass


@login_required
def profile(request):
    pass
