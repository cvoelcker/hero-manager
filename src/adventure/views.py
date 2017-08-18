from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView

from .models import DiaryEntry, Adventure
from hero.models import Group


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
        group = Group.objects.get(name=self.kwargs['group'])
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
    template_name = 'add_diary_entry.html'
