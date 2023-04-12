from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Todo, TodoItems
from .forms import TodoForm
# Create your views here.


def  home(request): 


    return render(request , 'home.html')



def Html(request):

    todos = Todo.objects.all()
    context = {"todos": todos}


    return render(request, 'home.html', context)


def details(request, id ):

  
    todo = Todo.objects.get(id = id)
    items = todo.todoitems_set.all()
    context={
        "todo": todo,
        "items" :items
    }
    return render(request , 'details.html' , context)



def create(request ):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'create.html' , context)


def update(request , pk):
    todo = Todo.objects.get(id = pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'update.html' , context)