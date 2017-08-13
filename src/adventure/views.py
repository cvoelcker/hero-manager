from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import DiaryEntry, Adventure


class DiaryView(LoginRequiredMixin, DetailView):
    model = DiaryEntry
    template_name = "diary_entry_view.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        self.kwargs
        return queryset.get(hero=self.kwargs[''])



class AdventureView(LoginRequiredMixin, DetailView):
    pass


class AdventureListView(LoginRequiredMixin, ListView):
    pass


@login_required
def diaries_list(request):
    pass
