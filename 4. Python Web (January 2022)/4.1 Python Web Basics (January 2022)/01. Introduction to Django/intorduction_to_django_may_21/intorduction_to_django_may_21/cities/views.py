from django.shortcuts import render

from intorduction_to_django_may_21.cities.models import Person


def index(req):
    # req = request object
    context = {
        "name": "Zaho",
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
