from django.http import HttpResponseRedirect
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
        user = self.request.user
        print(self.object.players.all())
        if user in self.object.players.all() and not user.hero_set.filter(
                group=self.object).exists():
            return redirect(
                reverse_lazy('hero:group_add_hero', kwargs=self.kwargs))

        else:
            return super(GroupDetailView, self).render_to_response(context)


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

    def form_valid(self, form):
        group = Group(
            name=form.cleaned_data['name'],
            rule_version=form.cleaned_data['rule_version'],
            players=form.cleaned_data['players'],
            description=form.cleaned_data['description'],
            game_master=self.request.user

        )
        group.save()
        return HttpResponseRedirect(self.get_success_url())

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

    def get_form_kwargs(self):
        # pass "user" keyword argument with the current user to your form
        kwargs = super(CreateView, self).get_form_kwargs()
        kwargs['player'] = self.request.user
        kwargs['group'] = Group.objects.get(name=self.kwargs['group'])
        return kwargs

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView

from .models import DiaryEntry, Adventure
from hero.models import Group, Hero


class AdventureView(LoginRequiredMixin, DetailView):
    model = Adventure
    template_name = "adventure_overview.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        group = Group.objects.get(name=self.kwargs['group'])
        context['group'] = group
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        group = Group.objects.get(name=self.kwargs['group'])
        return queryset.get(group=group, name=self.kwargs['adventure'])


class DiaryView(LoginRequiredMixin, ListView):
    model = DiaryEntry
    template_name = 'diary_overview.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        hero = Hero.objects.get(name=self.kwargs['hero'])
        group = hero.group
        context['group'] = group
        return context


class DiaryEntryView(LoginRequiredMixin, DetailView):
    model = DiaryEntry
    template_name = "diary_entry.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset


class AddDiaryEntryView(LoginRequiredMixin, CreateView):
    model = DiaryEntry
    fields = ('name', 'date', 'entry', 'hero')
    template_name = 'add_diary_entry.html'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['adventure'] = Adventure.objects.get(
            name=self.kwargs['adventure'])
        return context

    def form_valid(self, form):
        adventure = Adventure.objects.get(name=self.kwargs['adventure'])
        diary_entry = DiaryEntry(
            name=form.cleaned_data['name'],
            date=form.cleaned_data['date'],
            entry=form.cleaned_data['entry'],
            hero=form.cleaned_data['hero'],
            adventure=adventure,
        )
        diary_entry.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print(form.errors)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('adventure:hero_adventure_diary',
                       args=(self.kwargs['hero'], self.kwargs['adventure']))
