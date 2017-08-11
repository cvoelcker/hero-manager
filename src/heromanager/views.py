from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView


@csrf_exempt
def register(request, success=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero:home'))
        return HttpResponseRedirect('r')

    if not success:
        template = 'registration/registration_form.html'
    else:
        template = 'registration/registration_unsuccessful.html'
    return render(request, template, {})


class AboutView(TemplateView):
    template_name = 'about.html'
