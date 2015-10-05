from django.shortcuts import render


def home_view(request, template='index.html'):
    return render(request, template)
