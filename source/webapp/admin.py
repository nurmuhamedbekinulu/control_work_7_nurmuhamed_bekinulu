from django.contrib import admin
from webapp.models import Entry


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_mailbox', 'text', 'created_at', 'updated_at', 'status')
    list_filter = ('id', 'author_name', 'author_mailbox', 'status')
    search_fields = ('author_name', 'author_mailbox', 'status')
    fields = ('author_name', 'author_mailbox', 'text', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Entry, EntryAdmin)
        