from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Entry


def index_view(request: WSGIRequest):
    entries = Entry.objects.exclude(status='in blocked')
    context = {
        'entries': entries
    }
    return render(request, 'index.html', context=context)
