from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request, success=True):
    if request.method == 'POST':
        print("POSTING {}\n\n\n\n\n\n\n\n\n\n".format(request.POST))
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero:home'))
        return HttpResponseRedirect('register')
    
    if success:
        template = 'registration/registration_form.html'
    else:
        template = 'registration/registration_unsuccessful.html'
    return render(request, template, {})

