from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def home(request):
    task = Task.objects.all()
    form = TaskForm()
    
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/')
    context = {'tasks':task,'form':form}
    return render(request,'tasks/home.html',context)


def update(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save(commit=True)

        return redirect('/')
    context = {'task':task,'form':form}
    return render(request,'tasks/update.html',context)


def delete(request,pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task':task}
    return render(request,'tasks/delete.html',context)


