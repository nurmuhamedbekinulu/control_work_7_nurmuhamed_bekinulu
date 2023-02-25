from django.urls import path
from webapp.views.base import index_view
from webapp.views.entries import add_view, detail_view, update_view, delete_view, confirm_delete


urlpatterns = [
    path("", index_view, name='index'),
    path("entry/", index_view),
    path("entry/add/", add_view, name='entry_add'),
    path("entry/<int:pk>", detail_view, name='entry_detail'),
    path("entry/<int:pk>/update/", update_view, name='entry_update'),
    path("entry/<int:pk>/delete/", delete_view, name='entry_delete'),
    path("entry/<int:pk>/confirm_delete/", confirm_delete, name='confirm_delete'),
]
