from django.shortcuts import render
from .models import ToDo

# Create your views here.
def index(request):
    all_todos = ToDo.objects.exclude(status="DONE").order_by('-id')
    # data = []
    # for todo in all_todos:
    #     data.append(todo.id)


    context = {
        "title": "Home",
        # "data": data,
        "todos": all_todos
    }
    return render(request, 'kanban/home.html', context)

def list_todos(request):
    all_todos = ToDo.objects.order_by('-id')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def cards(request):
    all_todos = ToDo.objects.order_by('-id')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def show_backlog(request):
    all_todos = ToDo.objects.filter(status="BACKLOG").order_by('-created')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def show_todos(request):
    all_todos = ToDo.objects.filter(status="TODO").order_by('-updated')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def show_doing(request):
    all_todos = ToDo.objects.filter(status="DOING").order_by('-id')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def show_done(request):
    all_todos = ToDo.objects.filter(status="DONE").order_by('-updated')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/list.html', context)

def show_kanban(request):
    all_todos = ToDo.objects.exclude(status="DONE").order_by('-updated')

    context = {
        "title": "List All Todos",
        "todos": all_todos
    }
    return render(request, 'kanban/kanban.html', context)