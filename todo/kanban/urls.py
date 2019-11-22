from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list_todos, name="list_todos"),
    path("cards", views.cards, name="cards"),
    path("backlog", views.show_backlog, name="show_backlog"),
    path("todo", views.show_todos, name="show_todos"),
    path("doing", views.show_doing, name="show_doing"),
    path("done", views.show_done, name="show_done"),
    path("kanban", views.show_kanban, name="show_kanban")
]