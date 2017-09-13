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
    fields = ('name', 'date', 'entry')
    template_name = 'add_diary_entry.html'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['adventure'] = Adventure.objects.get(
            name=self.kwargs['adventure'])
        context['hero'] = Hero.objects.get(name=self.kwargs['hero'])
        return context

    def form_valid(self, form):
        adventure = Adventure.objects.get(name=self.kwargs['adventure'])
        hero = Hero.objects.get(name=self.kwargs['hero'])
        diary_entry = DiaryEntry(
            name=form.cleaned_data['name'],
            date=form.cleaned_data['date'],
            entry=form.cleaned_data['entry'],
            hero=hero,
            adventure=adventure,
        )
        diary_entry.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('adventure:hero_adventure_diary',
                       args=(self.kwargs['hero'], self.kwargs['adventure']))
