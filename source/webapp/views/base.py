from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Entry


def index_view(request: WSGIRequest):
    entries = Entry.objects.all()
    # entries = Entry.objects.exclude(is_deleted=True)
    context = {
        'entries': entries
    }
    return render(request, 'index.html', context=context)
