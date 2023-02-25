from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from static.classes.static import Static


def add_view(request: WSGIRequest):
    errors = {}

    if request.method == "GET":
        return render(request, 'entry_create.html', context={'choices': Static.choices})

    entry_data = {
        'author_name': request.POST.get('author_name'),
        'author_mailbox': request.POST.get('author_mailbox'),
        'text': request.POST.get('text')
    }
    if not request.POST.get('author_name'):
        errors['author_name'] = 'Поле с именем обязательно к заполнению'

    if not request.POST.get('author_mailbox'):
        errors['author_mailbox'] = 'Поле с почтой обязательно к заполнению'

    if not request.POST.get('text'):
        errors['text'] = 'Поле с текстом записи обязательно к заполнению'

    if errors:
        return render(request, 'entry_create.html',
                      context={
                          'errors': errors
                      })
    else:
        entry = Entry.objects.create(**entry_data)
        return redirect('index')


def update_view(request, pk):
    errors = {}

    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        if not request.POST.get('author_name'):
            errors['author_name'] = 'Поле с именем обязательно к заполнению'

        if not request.POST.get('author_mailbox'):
            errors['author_mailbox'] = 'Поле с почтой обязательно к заполнению'

        if not request.POST.get('author_name'):
            errors['text'] = 'Поле с текстом записи обязательно к заполнению'

        entry.author_name = request.POST.get('author_name')
        entry.author_mailbox = request.POST.get('author_mailbox')
        entry.text = request.POST.get('text')
        if errors:
            return render(request, 'entry_update.html',
                          context={
                              'entry': entry,
                              'errors': errors
                          })
        entry.save()
        return redirect('index')
    return render(request, 'entry_update.html', context={'entry': entry})


def delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry_confirm_delete.html', context={'entry': entry})


def confirm_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return redirect('index')
