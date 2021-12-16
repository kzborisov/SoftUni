from django.http import HttpResponse

from django.shortcuts import render


def people(req):
    return HttpResponse("This will show all the people!")


def list_phones(req):
    context = {
        'phones': [
            'Samsung',
            'IPhone',
            'Huawei',
            'Samsung',
            'IPhone',
            'Huawei',
        ]
    }
    return render(req, "phones.html", context)
