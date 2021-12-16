from django.shortcuts import render

from mysite_old.people.models import People


def index(req):
    context = {
        "name": "Zaho",
        'people': People.objects.all(),
    }
    return render(req, 'index.html', context)
