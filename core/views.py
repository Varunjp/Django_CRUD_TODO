from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import todo


# Create your views here.


def home(request):
    form = TodoForm
    todos = todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home.html',{'form':form, 'todos':todos})


def update(request, todo_id):
    todos = todo.objects.get(id=todo_id)
    form = TodoForm(instance=todos)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {'form':form})


def delete(request, todo_id):
    if request.method == 'POST':
        todo.objects.get(id=todo_id).delete()
        return redirect('home')
