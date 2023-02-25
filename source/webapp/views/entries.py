from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from django.http import HttpResponseNotFound
from django.urls import reverse
from static.classes.static import Static


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'entry_create.html', context={'choices': Static.choices})

    entry_data = {
        'author_name': request.POST.get('author_name'),
        'author_mailbox': request.POST.get('author_mailbox'),
        'text': request.POST.get('text'),
        'created_at': request.POST.get('created_at'),
        'updated_at': request.POST.get('updated_at'),
        'status': request.POST.get('status')
    }
    entry = Entry.objects.create(**entry_data)
    return redirect('entry_detail', pk=entry.pk)


def detail_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry.html', context={
        'entry': entry
    })


def update_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        entry.author_name = request.POST.get('author_name')
        entry.author_mailbox = request.POST.get('author_mailbox')
        entry.text = request.POST.get('text')
        entry.status = request.POST.get('status')
        entry.save()
        return redirect('entry_detail', pk=entry.pk)
    return render(request, 'entry_update.html', context={'entry': entry, 'choices': Static.choices})


def delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry_confirm_delete.html', context={'entry': entry})


def confirm_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return redirect('index')
