from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Home",
        "data": "Hello World"
    }
    return render(request, 'kanban/home.html', context)