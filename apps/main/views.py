import json
from .models import Message
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
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
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(reverse('home'))
    return render(request, template, dict(form=form))


def chat_add(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps(dict(success=True)),
                            content_type='application/json')
    return HttpResponse(
        json.dumps(dict(success=False, error_msg='invalid form')),
        content_type='application/json'
    )


def chat_get(request):
    return HttpResponse(
        serializers.serialize('json', Message.objects.all()),
        content_type='application/json'
    )
