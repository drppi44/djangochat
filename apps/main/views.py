from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from .forms import MessageForm
from django.shortcuts import render, redirect


def home_view(request, template='index.html'):
    if request.user.is_authenticated():
        return render(request, template, dict(form=MessageForm()))
    return render(request, template)


def registration(request, template='registration/registration.html'):
    if request.method == 'GET':
        context = dict(form=UserCreationForm())
        return render(request, template, context)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    return render(request, template, dict(form=form))
