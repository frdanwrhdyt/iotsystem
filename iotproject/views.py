from django.http import request
from django.shortcuts import render


def index(request):
    context = {
        "title": "Ngewasi",
        'link': 'login',
    }
    return render(request, 'index.html', context)
