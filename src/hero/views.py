from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView, CreateView, \
    UpdateView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from . import xml_hero
from .models import Group, Hero
from .forms import GroupForm, HeroAddForm, CharsheetUploadForm


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
        return queryset.get(name=self.kwargs['group'])

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.hero_set.filter(group=self.object).exists():
            return super(GroupDetailView, self).render_to_response(context)
        else:
            return redirect(
                reverse_lazy('hero:group_add_hero', kwargs=self.kwargs))


class GroupAdminView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups_all.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        user = self.request.user
        context['gm_groups'] = user.gaming_group_master.all()
        context['player_groups'] = user.gaming_group.all()
        return context


class GroupAddView(LoginRequiredMixin, CreateView):
    template_name = 'groups_add.html'
    form_class = GroupForm

    def get_success_url(self):
        return reverse_lazy('hero:group_detail', args=(self.object.name,))


class PlayerDetailView(LoginRequiredMixin, DetailView):
    pass


class GroupAddHeroView(LoginRequiredMixin, CreateView):
    template_name = "groups_add_hero.html"
    form_class = HeroAddForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['group_name'] = self.kwargs['group']
        return context

    def get_success_url(self):
        return reverse('hero:group_detail', args=(self.kwargs['group'],))


class ProfileView(LoginRequiredMixin, DetailView):
    pass


class HeroCharsheetView(DetailView):
    model = Hero
    template_name = "hero_charsheet.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get(name=self.kwargs['hero'],
                            group=self.kwargs['group'])

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            context['charsheet'] = xml_hero.get_hero(
                self.object.group.rule_version,
                self.object.char_sheet.read())
        finally:
            return context

    def get(self, request, *args, **kwargs):
        if not self.get_object().char_sheet:
            self.template_name = "no_charsheet.html"
        return super(HeroCharsheetView, self).get(self, request, *args,
                                                  **kwargs)


class GroupHeroView(LoginRequiredMixin, DetailView):
    pass


class HeroAddCharsheetView(LoginRequiredMixin, UpdateView):
    model = Hero
    fields = ['char_sheet']
    template_name = 'charsheet_upload.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get(name=self.kwargs['hero'],
                            group=self.kwargs['group'])

    def get_success_url(self):
        print(self.kwargs['group'])
        return reverse('hero:group_detail', args=(self.kwargs['group'],))
