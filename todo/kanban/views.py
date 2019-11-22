from django.shortcuts import render
from .models import ToDo

# Create your views here.
def index(request):
    all_todos = ToDo.objects.exclude(status=4).order_by('-id')
    data = []
    for todo in all_todos:
        data.append(todo.status)


    context = {
        "title": "Home",
        "data": data,
        "todos": all_todos
    }
    return render(request, 'kanban/home.html', context)